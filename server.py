from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from models import connect_to_db, db, Business, Rating, User
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

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
    return render_template('splash.html',
                           keys=helper.KEYS,
                           user=session.get("user_name"))


@app.route('/login', methods=['GET'])
def login_prompt():
    """Login page"""
    return render_template('log-in.html',
                           keys=helper.KEYS,
                           user=session.get("user_name"))


@app.route('/login', methods=['POST'])
def login():
    """logs in user"""
    form_data = request.form

    helper.login(form_data)
    return redirect('/')

@app.route('/logout')
def logout():
    """logs out user"""
    session['user_name'] = None
    session['user_id'] = None
    # todo fix flash
    flash("You are now logged out")
    return redirect('/')

@app.route('/create-account', methods=['GET'])
def acct_creation():
    """account creation page"""
    return render_template("user-add.html",
                           keys=helper.KEYS,
                           user=session.get("user_name"))


@app.route('/create-account', methods=['POST'])
def post_account():
    """creates user account"""
    form_data = request.form

    status = helper.add_user(form_data)
    flash(status)
#     todo add flash "your account has been created" & "you have been logged in"
    if status == "That username already exists":
        return render_template('user-add.html',
                               keys=helper.Keys,
                               user=session.get("user_name"))

    else:
        return redirect('/')


@app.route('/results')
def results():
    # todo finish me
    """search results page"""
    form_data = request.args
    location = helper.current_loc()
    result = helper.splash_query(form_data, (location['city'], location['region_code']))

    businesses = result[0]
    result_offset = result[1]
    result_count = result[2]
    print type(businesses)
    print businesses
    for business in businesses.values():
        print type(business)
        print business['name']
    return render_template('results.html',
                           form_data=form_data,
                           location=location,
                           keys=helper.KEYS,
                           user=session.get("user_name"),
                           businesses=businesses,
                           offset=result_offset,
                           total=result_count)


@app.route('/results/<int:offset>')
def more_results(offset):
    form_data = request.args
    location = helper.current_loc()
    result = helper.splash_query(form_data, (location['city'], location['region_code']), offset)

    businesses = result[0]
    result_offset = result[1]
    result_count = result[2]
    print type(businesses)
    print businesses
    for business in businesses.values():
        print type(business)
        print business['name']
    return render_template('results.html',
                           form_data=form_data,
                           location=location,
                           keys=helper.KEYS,
                           user=session.get("user_name"),
                           businesses=businesses,
                           offset=result_offset,
                           total=result_count)


@app.route('/explore')
def explore():
    """explore page"""
    return render_template('construction.html',
                           keys=helper.KEYS,
                           user=session.get("user_name"))


@app.route('/<string:username>')
def user_account(username):
    """User account page"""
    return render_template('construction.html',
                           keys=helper.KEYS,
                           user=session.get("user_name"))


@app.route('/<string:username>/')
def favorites(username):
    """user favorites"""
    return render_template('construction.html',
                           keys=helper.KEYS,
                           user=session.get("user_name"))


@app.route('/<string:username>/ratings')
def ratings(username):
    """user ratings"""
    return render_template('construction.html',
                           keys=helper.KEYS,
                           user=session.get("user_name"))


@app.route('/info/<string:business>')
def info(business):
    return render_template('construction.html',
                           keys=helper.KEYS,
                           user=session.get("user_name"))


@app.route('/info/<string:business>/rate', methods=['GET'])
def rate(business):
    """presents user with form to rate business"""
    # converts id from yelp_id to business_id if applicable, then returns appropriate object
    business_info = helper.return_business_object(helper.find_bus_id(business))

    return render_template('rating-form.html',
                           business_name=business_info.name,
                           business_id=business,
                           user=session.get("user_name"))


@app.route('/info/:business/rate', methods=['POST'])
def submit_review(business):
    """submits review and redirects back to the business page"""
    # determines whether business in url is from yelp API or local only
    form_data = request.form
    user_id = session['user_id']
    helper.add_rating(form_data, business, user_id)

    # todo add flash "your rating has been submitted"
    return redirect("/info/:business")


@app.route('/:username/manage')
def account_manage(username):
    """allows update of user information. Requires new login"""
    return render_template('construction.html',
                           keys=helper.KEYS,
                           user=session.get("user_name"))


if __name__ == '__main__':
    # toggles debug mode on
    app.debug = True

    # runs debug toolbar
    DebugToolbarExtension(app)

    # connects to database
    connect_to_db(app)

    # # runs app
    app.run()
