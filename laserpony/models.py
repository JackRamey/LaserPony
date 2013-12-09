import datetime

from flask_login import AnonymousUserMixin
from util import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)

class User(db.Document):
    name = db.StringField(max_length=64, required=True)
    email = db.StringField(max_length=254)
    password_hash = db.StringField(required=True)
    active = db.BooleanField()
    admin = db.BooleanField(default=False)
    anonymous = db.BooleanField(default=False)
    authenticated = db.BooleanField()

    def check_password(self, password):
            return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def is_active(self):
        return self.active

    def is_admin(self):
        return self.admin

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def get_id(self):
        return self.name

    def __repr__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.name, self.email)

    def __str__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.name, self.email)

    def __unicode__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.name, self.email)

class Anonymous(AnonymousUserMixin):
    def is_admin(self):
        return False

@login_manager.user_loader
def load_user(userid):
    return User.objects.get(name=userid)

login_manager.anonymous_user = Anonymous

