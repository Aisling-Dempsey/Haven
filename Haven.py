from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from models import connect_to_db
import os


app = Flask(__name__)

# makes jinja throw error if requesting undefined value
app.jinja_env.undefined = StrictUndefined

# gets secret key from secrets.sh
SECRET_KEY = os.environ['HAVEN_SECRET_KEY']
app.secret_key= SECRET_KEY

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # toggles debug mode on
    app.debug = True

    # runs debug toolbar
    DebugToolbarExtension(app)

    # connects to database
    connect_to_db(app)

    # runs app
    app.run()
