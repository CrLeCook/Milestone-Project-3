from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Optional

class TodoForm(FlaskForm):
    name = StringField('name of task', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    completed = SelectField('completed?', choices=[("False", "No"), ("True", "Yes")], validators=[DataRequired()])
    submit = SubmitField("create Task!")

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('register')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember Me')
    submit = SubmitField('login')
    
class AccountForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('new password', validators=[DataRequired()])
    submit = SubmitField('update password')
