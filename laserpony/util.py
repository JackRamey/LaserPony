from laserpony import app
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask.ext.markdown import Markdown
from flask_mongoengine import MongoEngine

#Bcrypt
bcrypt = Bcrypt(app)

#Login Manager
login_manager = LoginManager(app)

#Markdown Parser
markdown = Markdown(app)

#Database
db = MongoEngine(app)

