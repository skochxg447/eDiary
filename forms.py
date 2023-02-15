from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields import SelectMultipleField


class AddEntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    tag = SelectMultipleField('tag')
    submit = SubmitField('Submit')

class DeleteEntryForm(FlaskForm):
    submit = SubmitField('Delete')
