from wtforms.form import Form
from wtforms import Field, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = Field('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
