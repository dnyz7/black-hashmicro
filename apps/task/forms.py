from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    task_info = StringField('Task Info',
                         id='task_info',
                         validators=[DataRequired()])
    task_name = StringField('Task Name',
                         id='task_name',
                         validators=[DataRequired()])