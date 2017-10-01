from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class NameInput(Form):
    name1 = StringField('name1', validators=[DataRequired()])
    name2 = StringField('name2', validators=[DataRequired()])
