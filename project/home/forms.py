from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Length


class MessageForm(Form):
    title = TextField('Title', validators=[DataRequired(), Length(max=128)])
    description = TextField('Description', validators=[DataRequired(), Length(max=512)])
