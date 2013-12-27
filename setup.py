from laserpony import app
from laserpony.util import db
from laserpony.models.user import User

#Check if any users exist in the system
if len(User.objects) == 0:
    name = app.config['DEFAULT_ADMIN_NAME']
    email = app.config['DEFAULT_ADMIN_EMAIL']
    password = app.config['DEFAULT_ADMIN_PASSWORD']
    admin = User.create_user(name,email,password)
    admin.active = True
    admin.admin = True
    admin.authenticated = True
    admin.author = True
    admin.save()

