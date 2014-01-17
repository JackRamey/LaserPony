from flask import Flask

#Create the app
app = Flask(__name__)
app.config.from_pyfile('laserpony.cfg', silent=False)

from views.index import *
from views.post import *
from views.user import *
