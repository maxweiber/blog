from app import app, lm, oid, db
from flask import Flask, render_template, flash, redirect, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from .form import loginForm
from .models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = "Index")

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login', methods=['GET','POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = loginForm()
    if form.validate_on_submit():
        flash('Your OpenID is '+form.openid.data+'. Remember me is '+str(form.remember_me.data))
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html', title = "Login", form = form, providers = app.config['OPENID_PROVIDERS'])
