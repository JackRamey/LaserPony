from flask_login import AnonymousUserMixin
from laserpony.util import bcrypt, db, login_manager


class User(db.Document):
    name = db.StringField(max_length=64, required=True)
    email = db.StringField(max_length=254)
    password_hash = db.StringField(required=True)
    active = db.BooleanField(default=False)
    admin = db.BooleanField(default=False)
    anonymous = db.BooleanField(default=False)
    authenticated = db.BooleanField(default=False)
    author = db.BooleanField(default=False)

    def check_password(self, password):
            return bcrypt.check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def is_active(self):
        return self.active

    def is_admin(self):
        return self.admin

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def is_author(self):
        return self.author

    def get_id(self):
        return self.name

    def __repr__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.name, self.email)

    def __str__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.name, self.email)

    def __unicode__(self):
        return '<%s: %s, %s>' % (self.__class__.__name__, self.name, self.email)


class Anonymous(AnonymousUserMixin):

    def is_author(self):
        return False

    def is_admin(self):
        return False

@login_manager.user_loader
def load_user(userid):
    return User.objects(name=userid).first()

login_manager.anonymous_user = Anonymous

def create_user(name, email, password):
    newUser = User(name,email)
    newUser.set_password(password)
    newUser.save()
    return newUser

