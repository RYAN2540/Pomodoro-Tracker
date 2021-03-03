from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, StringField, BooleanField, IntegerField
from wtforms.validators import Required, Email, Length

class LoginForm(FlaskForm):
	username = StringField('Username', validators = [Required(), Length(min=4, max=15)])
	password = PasswordField('Password', validators = [Required(), Length(min=8, max=80)])
	remember = BooleanField('Remember me')


class RegisterForm(FlaskForm):
	email = StringField('Email', validators = [Required(), Email(message='Invalid Email')])
	username = StringField('Username', validators = [Required(), Length(min=4, max=15)])
	password = PasswordField('Password', validators = [Required(), Length(min=8, max=80)])