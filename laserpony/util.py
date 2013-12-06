from laserpony import app
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

#Database
db = MongoEngine(app)

#Login Manager
login_manager = LoginManager(app)

