from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from models import connect_to_db, db, Business, Rating, User

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




# EXAMPLE YELP QUERIES
# search_results = yelp_api.search_query(args)
# business_results = yelp_api.business_query(id=business_id, other_args)
# phone_search_results = yelp_api.phone_search_query(phone=phone_number, other_args)

def hello_world():
    return 'Hello World!'


@app.route('/')
def splash():
    """splash page"""
    return render_template('splash.html', keys=helper.KEYS)


@app.route('/login')
def login():
    """Login page"""
    return render_template('construction.html', keys=helper.KEYS)


@app.route('/create-account', methods=['GET'])
def acct_creation():
    """account creation page"""
    return render_template("user-add.html")


@app.route('/create-account', methods=['POST'])
def post_account():
    form_data = request.form

    helper.add_user(form_data)
#     todo add flash "your account has been created" & "you have been logged in"
    return redirect('/')



@app.route('/results')
def results():
    """search results page"""
    return render_template('construction.html', keys=helper.KEYS)


@app.route('/explore')
def explore():
    """explore page"""
    return render_template('construction.html', keys=helper.KEYS)


@app.route('/:username')
def user_account(username):
    """User account page"""
    return render_template('construction.html', keys=helper.KEYS)


@app.route('/:username/favorites')
def favorites(username):
    """user favorites"""
    return render_template('construction.html', keys=helper.KEYS)


@app.route('/:username/ratings')
def ratings(username):
    """user ratings"""
    return render_template('construction.html', keys=helper.KEYS)


@app.route('/info/:business')
def info(business):
    return render_template('construction.html', keys=helper.KEYS)


@app.route('/info/:business/rate', methods=['GET'])
def rate(business):
    """presents user with form to rate business"""
    # converts id from yelp_id to business_id if applicable, then returns appropriate object
    business_info = helper.return_business_object(helper.find_bus_id(business))

    return render_template('rating-form.html',
                           business_name=business_info.name,
                           business_id=business
                           )


@app.route('/info/:business/rate', methods=['POST'])
def submit_review(business):
    """submits review and redirects back to the business page"""
    # determines whether business in url is from yelp API or local only
    form_data = request.form

    helper.add_rating(form_data, business)

    # todo add flash "your rating has been submitted"
    return redirect("/info/:business")


@app.route('/:username/manage')
def account_manage(username):
    """allows update of user information. Requires new login"""
    return render_template('construction.html', keys=helper.KEYS)


if __name__ == '__main__':
    # toggles debug mode on
    app.debug = True

    # runs debug toolbar
    DebugToolbarExtension(app)

    # connects to database
    connect_to_db(app)

    # runs app
    app.run()
