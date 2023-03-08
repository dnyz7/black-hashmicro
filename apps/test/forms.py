from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    username = StringField('Task Info',
                         id='task_info',
                         validators=[DataRequired()])
    password = StringField('Task Name',
                         id='task_name',
                         validators=[DataRequired()])