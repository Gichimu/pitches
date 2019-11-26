from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

class pitchForm(FlaskForm):
    body = TextAreaField('Enter your 1 minute pitch here...', validators=[Required()])
    submit = SubmitField('Submit')