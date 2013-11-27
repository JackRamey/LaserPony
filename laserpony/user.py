from util import db, login_manager
from flask_login import AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Document):
    name = db.StringField(max_length=64, required=True)
    email = db.StringField(max_length=254)
    password = db.StringField()
    authenticated = db.BoolField()
    active = db.BoolField()
    admin = db.BoolField()

    def __init__(self, name, email, password,
                active=False, admin=False, authenticated=False):
        self.name = name
        self.email = email
        self.password = set_password(password)
        self.active = active
        self.admin = admin
        self.authenticated = authenticated

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


class Anonymous(AnonymousUserMixin):
    def is_admin(self):
        return False

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.name == userid).first()

login_manager.anonymous_user = Anonymous

