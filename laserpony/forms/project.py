from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

class ProjectForm(Form):
    name = TextField('name', validators=[DataRequired()])
    slug = TextField('slug', validators=[DataRequired()])

