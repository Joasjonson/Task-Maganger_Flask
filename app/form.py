from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])
    priority = SelectField('Priority', choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], validators=[DataRequired()])
    status = SelectField('Status', choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], validators=[DataRequired()])




    