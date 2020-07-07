from flask_wtf import FlaskForm
from wtforms import SubmitField

class GenerateTrickButton(FlaskForm):
    submit = SubmitField('Generate Trick')
