from flask.ext.wtf import Form
from wtforms import StringField, BooleanFiled
from wtforms.validators import DataRequired

class loginForm(Form):
    openid = StringField('OpenID', validators = [DataRequired()])
    remember_me = BooleanFiled('Remember me', default = False)
