from laserpony import app
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask.ext.markdown import Markdown

#Database
db = MongoEngine(app)

#Login Manager
login_manager = LoginManager(app)

#Markdown Parser
Markdown(app)

