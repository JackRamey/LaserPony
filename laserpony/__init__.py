from flask import Flask

#Create the app
app = Flask(__name__)
app.config.from_pyfile('laserpony.cfg', silent=True)

import views
