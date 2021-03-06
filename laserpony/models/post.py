import datetime

from laserpony.util import db
from laserpony.models.user import User
from laserpony.models.project import Project


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    author = db.ReferenceField(User)
    project = db.ReferenceField(Project)

    def __repr__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.title, self.slug)

    def __str__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.title, self.slug)

    def __unicode__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.title, self.slug)

