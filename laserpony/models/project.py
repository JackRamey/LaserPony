from flask import g
from laserpony.util import db


class Project(db.Document):
    name = db.StringField(max_length=25, required=True)
    slug = db.StringField(max_length=25, required=True)

