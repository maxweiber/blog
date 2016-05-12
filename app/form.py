from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class loginForm(Form):
    openid = StringField('OpenID', validators = [DataRequired()])
    remember_me = BooleanField('Remember me', default = False)
