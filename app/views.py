from app import app
from flask import Flask, render_template, flash, redirect
from .form import loginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = "Index")

@app.route('/login', methods=['GET','POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        flash('Your OpenID is '+form.openid.data+'. Remember me is '+str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = "Login", form = form, providers = app.config['OPENID_PROVIDERS'])
