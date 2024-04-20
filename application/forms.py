from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    name = StringField('name of task', validators=[DataRequired()])
    description = TextAreaField('description',validators=[DataRequired()])
    completed = SelectField('completed?', choices = [("False", "yes"), ("True", "no")], validators = [DataRequired()])
    submit = SubmitField("create task!")