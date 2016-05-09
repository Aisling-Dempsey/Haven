from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from models import connect_to_db
from yelpapi import YelpAPI
import helper

import os


app = Flask(__name__)

# makes jinja throw error if requesting undefined value
app.jinja_env.undefined = StrictUndefined

# gets secret key from secrets.sh


SECRET_KEY = os.environ['HAVEN_SECRET_KEY']
app.secret_key = SECRET_KEY


# dict of api keys to be passed into every render template for google maps api
KEYS = {'maps': os.environ['MAPS_SECRET_KEY']
        }

YELP_CONSUMER_KEY = os.environ['YELP_CONSUMER_KEY']
YELP_CONSUMER_SECRET = os.environ['YELP_CONSUMER_SECRET']
YELP_TOKEN = os.environ['YELP_TOKEN']
YELP_TOKEN_SECRET = os.environ['YELP_TOKEN_SECRET']


# instantiates yelp api with appropriate keys.
yelp_api = YelpAPI(YELP_CONSUMER_KEY, YELP_CONSUMER_SECRET, YELP_TOKEN, YELP_TOKEN_SECRET)


# EXAMPLE YELP QUERIES
# search_results = yelp_api.search_query(args)
# business_results = yelp_api.business_query(id=business_id, other_args)
# phone_search_results = yelp_api.phone_search_query(phone=phone_number, other_args)

def hello_world():
    return 'Hello World!'


@app.route('/')
def splash():
    """splash page"""
    return render_template('splash.html', keys=KEYS)


@app.route('/login')
def login():
    """Login page"""
    return render_template('construction.html', keys=KEYS)


@app.route('/results')
def results():
    """search results page"""
    return render_template('construction.html', keys=KEYS)


@app.route('/explore')
def explore():
    """explore page"""
    return render_template('construction.html', keys=KEYS)

@app.route('/:username')
def user_account(username):
    """User account page"""
    return render_template('construction.html', keys=KEYS)

@app.route('/:username/favorites')
def favorites(username):
    """user favorites"""
    return render_template('construction.html', keys=KEYS)

@app.route('/:username/ratings')
def ratings(username):
    """user ratings"""
    return render_template('construction.html', keys=KEYS)

@app.route('/:username/manage')
def account_manage(username)
    """allows update of user information. Requires new login"""
    return render_template('construction.html', keys=KEYS)

if __name__ == '__main__':
    # toggles debug mode on
    app.debug = True

    # runs debug toolbar
    DebugToolbarExtension(app)

    # connects to database
    connect_to_db(app)

    # runs app
    # app.run()
