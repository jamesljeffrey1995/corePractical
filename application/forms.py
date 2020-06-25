from wtforms import SubmitField
from flask_wtf import FlaskForm

class PostForm(FlaskForm):
    submit = SubmitField('Get Prize')
