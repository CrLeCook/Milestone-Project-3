from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

# Define a FlaskForm for creating a new todo
class TodoForm(FlaskForm):
    # StringField for the name of the task
    name = StringField('name of task', validators=[DataRequired()])
    
    # TextAreaField for the description of the task
    description = TextAreaField('description', validators=[DataRequired()])
    
    # SelectField for indicating whether the task is completed or not
    completed = SelectField('completed?', choices=[("False", "no"), ("True", "yes")], validators=[DataRequired()])
    
    # SubmitField for submitting the form to create the task
    submit = SubmitField("create task!")
