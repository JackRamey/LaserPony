from laserpony import app
from laserpony.util import db
from laserpony.models import User

#Check if any users exist in the system
if len(User.objects) == 0:
    name = app.config['DEFAULT_ADMIN_NAME']
    email = app.config['DEFAULT_ADMIN_EMAIL']
    password = app.config['DEFAULT_ADMIN_PASSWORD']
    admin = User(name,email,password,active=True,admin=True,authenticated=True)
    admin.save()

