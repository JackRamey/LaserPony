import sys

activate_this = '/var/www/LaserPony/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.append("/var/www/LaserPony")
from laserpony import app as application

