from flask.ext.mongoalchemy import MongoAlchemy
from flask_login import LoginManager
from laserpony import app

#Setup Database (MongoDB via MongoAlchemy)
db = MongoAlchemy(app)

#Setup Login Manager
login_manager = LoginManager()
login_manager.setup_app(app)

