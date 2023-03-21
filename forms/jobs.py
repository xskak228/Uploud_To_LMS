from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = StringField('TeamLeader', validators=[DataRequired()])
    job = StringField("Job", validators=[DataRequired()])
    work_size = StringField("Work Size", validators=[DataRequired()])
    collaborators = StringField("Collaborators", validators=[DataRequired()])
    start_date = StringField("Start Date")
    end_date = StringField("End Date")
    is_finished = BooleanField("Finished?")
    submit = SubmitField('Continue')