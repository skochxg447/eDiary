from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddEntryForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Submit")


class DeleteEntryForm(FlaskForm):
    submit = SubmitField("Delete")
