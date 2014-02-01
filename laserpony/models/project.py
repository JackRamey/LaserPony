from flask import g
from laserpony.util import db


class Project(db.Document):
    name = db.StringField(max_length=25, required=True)
    slug = db.StringField(max_length=25, required=True)

    def postCount(self):
        #Import here to prevent circular imports
        from laserpony.models.post import Post
        posts = Post.objects(project=self)
        return len(posts)

    def __repr__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.name, self.slug)

    def __str__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.name, self.slug)

    def __unicode__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.name, self.slug)

