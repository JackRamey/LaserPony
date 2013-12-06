from flask import Flask

#Create the app
app = Flask(__name__)
app.config.from_pyfile('laserpony.cfg', silent=False)

if not app.debug:
    import os
    import logging

    from logging import Formatter, FileHandler

    file_handler = FileHandler('error.log')
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ' '[in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

import views
