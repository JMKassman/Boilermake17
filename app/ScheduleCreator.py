from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class ScheduleCreator(Form):
    name = StringField('name', validators=[DataRequired()])
    course1 = StringField('course1', validators=[DataRequired()], default='NC')
    start_time1 = IntegerField('start_time1', default=0)
    end_time1 = IntegerField('end_time1', default=0)
    course2 = StringField('course2', validators=[DataRequired()], default='NC')
    start_time2 = IntegerField('start_time2', default=0)
    end_time2 = IntegerField('end_time2', default=0)
    course3 = StringField('course3', validators=[DataRequired()], default='NC')
    start_time3 = IntegerField('start_time3', default=0)
    end_time3 = IntegerField('end_time3', default=0)
    course4 = StringField('course4', validators=[DataRequired()], default='NC')
    start_time4 = IntegerField('start_time4', default=0)
    end_time4 = IntegerField('end_time4', default=0)
    course5 = StringField('course5', validators=[DataRequired()], default='NC')
    start_time5 = IntegerField('start_time5', default=0)
    end_time5 = IntegerField('end_time5', default=0)
