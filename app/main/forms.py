from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import Required

class pitchForm(FlaskForm):
    photo = FileField(validators=[Required()])
    body = TextAreaField('Enter your 1 minute pitch here...', validators=[Required()])
    submit = SubmitField('Submit')