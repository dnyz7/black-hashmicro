from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TestForm(FlaskForm):
    string1 = StringField('Input String 1',
                         id='string1',
                         validators=[DataRequired()])
    string2 = StringField('Input String 2',
                         id='string2',
                         validators=[DataRequired()])