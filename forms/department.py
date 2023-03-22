from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class DEpartment(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    chief = StringField("Chief", validators=[DataRequired()])
    members = StringField("Members", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField('Continue')