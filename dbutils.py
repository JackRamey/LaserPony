"""Usage: dbutils.py [-dfh]

Options:
    -d --dropall    Deletes all collections in the database. Use this very wisely.
    -f --force      Forces all questions to 'yes'
    -h --help       show this
"""
import sys
from docopt import docopt
from laserpony import app
from laserpony.util import db

##UTILITY FUNCTIONS

#snagged this from http://code.activestate.com/recipes/577058/
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")

# Switch over to the virtual environment version of python
arguments = docopt(__doc__, argv=sys.argv[1:], version='0.1')

delete_db_message = "Are you absolutely sure you want to delete the entire database?"

if arguments['--dropall']:
    if arguments['--force']:
        db.connection.drop_database(app.config['MONGODB_SETTINGS']['DB'])
    else:
        if query_yes_no(delete_db_message, default="no"):
            db.connection.drop_database(app.config['MONGODB_SETTINGS']['DB'])

