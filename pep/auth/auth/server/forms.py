from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField(
        'Email', validators=[DataRequired(), Email(message='Enter a valid email.')]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')