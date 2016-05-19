import requests
from models import Business, Rating, User, Category, BusinessCategory
from yelpapi import YelpAPI
from flask import session, request, jsonify
import os
from datetime import datetime
from models import connect_to_db, db
import sys
reload(sys)
sys.setdefaultencoding('UTF8')


KEYS = {'maps': os.environ['MAPS_SECRET_KEY'],
        'YELP_CONSUMER_KEY': os.environ['YELP_CONSUMER_KEY'],
        'YELP_CONSUMER_SECRET': os.environ['YELP_CONSUMER_SECRET'],
        'YELP_TOKEN': os.environ['YELP_TOKEN'],
        'YELP_TOKEN_SECRET': os.environ['YELP_TOKEN_SECRET']
}



# instantiates yelp api with appropriate keys.
yelp_api = YelpAPI(KEYS['YELP_CONSUMER_KEY'], KEYS['YELP_CONSUMER_SECRET'],
                   KEYS['YELP_TOKEN'], KEYS['YELP_TOKEN_SECRET'])


###### HELPER FUNCTIONS #####
def login(payload):
    """logs in user"""
    email = payload['email']
    password = payload['password']
    db_user = User.query.filter_by(email=email).first()

    # checks if user exists and then compares passwords. if they match, logs in user and sets session variables
    if db_user:
        if password == db_user.password:
            session['user_id'] = db_user.user_id
            session['user_name'] = db_user.name

            return "Logged in as", db_user.name

        else:
            return "That password is incorrect, please try again"

    else:
        return "That username does not exist"
# todo fail quick

def add_user(payload):
    """Takes form information as a dictionary and creates user account if it doesn't already exist"""
    email = payload['email']
    password = payload['password']
    name = payload['name']

    if not User.query.filter_by(email=email).first():
        user = User(email=email, name=name, password=password)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.user_id
        session['user_name'] = user.name


def get_ratings(user_id):
    """returns a dictionary of all of users ratings with sub-dicts of info about the ratings under the yelp_id"""
    ratings=User.query.get(user_id).ratings
    rating_info = {}
    for rating in ratings:
        date = rating.created_at.strftime("%B %d, %Y at %I:%M %p")
        rating_info[rating.business.yelp_id] = {'score': rating.score,
                                                'review': rating.review,
                                                'created_at': date,
                                                'business_name': rating.business.name}

    return rating_info

def current_loc():
    """outputs locational json based upon user ip"""
    r = requests.get("http://freegeoip.net/json/")
    location = r.json()
    return location


def yelp_by_id(yelp_ID):
    """returns a dictionary of yelp information using the Yelp ID"""
    return yelp_api.business_query(id=yelp_ID)



def add_business(info):
    """adds business to local db along with categories from a dictionary of yelp query results"""
    business = Business()

    # for search, add key ['businesses'] before these keys

    business.yelp_id = info['id']
    business.name = info['name']
    address = info['location'].get('address')
    # checks for an address and adds all applicable lines to information dictionary
    if address:
        business.address_line_1 = address[0]
        if len(address) > 1:
            business.address_line_2 = address[1]

    business.city = info['location']['city']
    business.state = info['location']['state_code']
    business.zipcode = info['location']['postal_code']

    if info.get('phone'):
        business.phone = info['phone']

    # checks for coordinates and adds them to information dictionary if they exist
    coordinates = info['location'].get('coordinate')
    if coordinates:
        business.latitude = coordinates['latitude']
        business.longitude = coordinates['longitude']

    # empty list of categories
    cat_list = []

    categories = info.get('categories')
    if categories:
        for group in categories:
            for category in group:
                if not Category.query.filter_by(category_name=category).first():
                    cat_list.append(category)
                    category = Category()
                    db.session.add(category)
            db.session.commit()

    # adds categories and business id to reference tables
    for cat in cat_list:
        # creates row in reference table
        catbus = BusinessCategory()

        catbus.business_id = business.business_id
        cat_object = Category.query.filter_by(category_name=cat).first()
        catbus.category_id = cat_object.category_id

        if not BusinessCategory.query.filter_by(business_id=catbus.business_id, category_id=catbus.category_id):
            db.session.add(catbus)
    db.session.commit()


    # temporary debug
    db.session.add(business)
    db.session.commit()


def find_bus_id(id_to_check):
    """validates whether an ID is a business_id or a yelp_id and returns the business_id"""
    try:
        return int(id_to_check)
    except ValueError:
        result = Business.query.filter_by(yelp_id=id_to_check).first()
        return result.business_id


def return_business_model(business_id):
    """returns the business model using the business_id. Often paired with find_bus_id(id_to_check)"""
    return Business.query.get(business_id)


def get_aggregate_rating(business):
    """takes business model and returns aggregate score and number of ratings as a tuple"""

    haven_ratings = business.ratings

    # todo refactor to helper function
    scores = []
    # todo list comprehension
    for rating in haven_ratings:
        scores.append(rating.score)
    total_score = 0
    score_count = 0
    for score in scores:
        total_score += score
        score_count += 1
    # TODO: check for divide by zero
    return round(total_score / float(score_count), 2), score_count


def validate_db(yelp_object, haven_model):
    """takes the result of a yelp query by businesses id and compares it to the database entry. If any information
     on the local db is out of date, it is updated accordingly."""

    # todo, check if exists, then set. commit all at the end.
    # todo try and refactor to use both for add and validation
    # idea: run query for haven_model inside and check if is none?

    if haven_model.name != yelp_object['name']:
        haven_model.name = yelp_object['name']
        db.session.commit()

    if yelp_object['location'].get('address'):
        if len(yelp_object['location']['address']) > 1:
            if haven_model.address_line_2 != yelp_object['location']['address'][1]:
                haven_model.address_line_2 = yelp_object['location']['address'][1]
        if haven_model.address_line_1 != yelp_object['location']['address'][0]:
            haven_model.address_line_1 = yelp_object['location']['address'][0]
        db.session.commit()

    # nothing in local db should not have a city and state code but if for some reason yelp wiped them, it prevents it
    # from being cleared, protecting db integrity
    if haven_model.city != yelp_object['location']['city'] and yelp_object['location'].get('city') is not None:
        haven_model.city = yelp_object['location']['city']
        db.session.commit()

    if haven_model.state != yelp_object['location']['state_code'] and yelp_object['location'].get('state_code') \
            is not None:
        haven_model.state = yelp_object['location']['state_code']
        db.session.commit()

    if yelp_object['location'].get('postal_code'):
        if haven_model.zipcode != yelp_object['location']['postal_code']:
            haven_model.zipcode = yelp_object['location']['postal_code']
        db.session.commit()

    if yelp_object.get('phone'):
        if haven_model.phone != yelp_object['phone']:
            haven_model.phone = yelp_object['phone']
        db.session.commit()

    if yelp_object['location'].get('coordinate'):
        if haven_model.latitude != yelp_object['location']['coordinate']['latitude']:
            haven_model.latitude = yelp_object['location']['coordinate']['latitude']
        if haven_model.longitude != yelp_object['location']['coordinate']['longitude']:
            haven_model.longitude = yelp_object['location']['coordinate']['longitude']
        db.session.commit()


def splash_query(term, location, offset):
    """takes search term, location (in city, state format) and offset.
        returns a tuple in the format (term, offset, company_info, total results) where
        company_info is a dict}
    """

    results = yelp_api.search_query(term=term, location=location, offset=offset)
    total_results = results['total']
    # loops through the displayed businesses and gives each one a sub dict with a key of the yelp id
    # while there are less than 10 results with an entry in the local db, loops through results and adds
    # any businesses with a haven review to a list by yelp_ids.
    company_info = {}
    # tries to build dict of 10 buesinesses, if less than 10, outputs availbable businesses.
    while len(company_info) < 10 and offset < total_results:
        # loops through yelp results to see if they exist in db, checking if there are less than 10 matching
        # results so far.
        for result in results['businesses']:
            # todo 'for result in yieldstuff, build stuff to handle exception'

            if len(company_info) < 10:
                yelp_id = result['id']
                offset += 1
                print "\n"
                print "looping through", offset

                business = Business.query.filter_by(yelp_id=yelp_id).first()
                if business:
                    name = business.name
                    photo = result['image_url']
                    category = business.categories[0].category_name
                    yelp_rating = result['rating']
                    ratings = get_aggregate_rating(business)

                    company_info[yelp_id] = {'photo': photo,
                                             'yelp_score': yelp_rating,
                                             'score': ratings[0],
                                             'total_ratings': ratings[1],
                                             'name': name,
                                             'category': category}

                    if business.address_line_1:
                        company_info[yelp_id]['address_line_1'] = business.address_line_1

                    if business.address_line_2:
                        company_info[yelp_id]['address_line_2'] = business.address_line_2

            else:
                return term, offset, company_info, total_results

        results = yelp_api.search_query(term=term, location=location, offset=offset)

    return term, offset, company_info, total_results

# todo look into me as a means of simplifying structure
# def yieldstuff():
#     while true:
#         results = yelp_api.search_query(term=term, location=location, offset=offset)
#         for

def add_rating(form_data, unknown_id):
    """adds a rating form data and business_id"""
    # sterilizes the id to return haven business_id regardless of whether it receives yelp_id or haven id
    business_id = find_bus_id(unknown_id)
    score = int(form_data.get("score"))
    review = form_data.get("review")
    created_at = datetime.now()

    rating = Rating(business_id=business_id,
                    user_id=session['user_id'],
                    score=score,
                    created_at=created_at)
    if review:
        rating.review = review

    db.session.add(rating)
    db.session.commit()

    return "Your rating has been added!"


def _example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    Rating.query.delete()
    BusinessCategory.query.delete()
    Business.query.delete()
    Category.query.delete()
    User.query.delete()

    # Add sample businesses and users
    hackbright = Business(business_id=999, yelp_id='hackbright-academy-san-francisco',
                          name='Hackbright Academy', city='San Francisco', state='CA')
    estellas = Business(business_id = 998, yelp_id='estelas-fresh-sandwiches-san-francisco',
                        name='Estella\'s', city='San Francisco', state='CA')
    # listing without yelp_id
    piraat = Business(business_id = 997, name='Piraat', city='San Francisco', state='CA')

    liz = User(user_id=999, name='Liz', email='liz@liz.com', password='liz_pass')
    leonard = User(user_id=998, name='Leonard', email='leonard@leonard.com', password='leonard_pass')
    leslie = User(user_id=997, name='Leslie', email='leslie@leslie.com', password='leslie_pass')

    db.session.add_all([hackbright, estellas, piraat, leonard, liz, leslie])
    db.session.commit()

    # add ratings and categories

    liz_rate = Rating(rating_id=999, user_id=999, business_id=999,
                      score=5, review="Awesome!", created_at=datetime.now())
    lenny_rate = Rating(rating_id=998, user_id=998, business_id=998,
                        score=3, created_at=datetime.now())

    hackbright_cat_1 = Category(category_id=999, category_name='Vocational & Technical School')
    hackbright_cat_2 = Category(category_id=998, category_name='vocation')

    estellas_cat_1 = Category(category_id=997, category_name='Delis')
    estellas_cat_2 = Category(category_id=996, category_name='delis')

    db.session.add_all([liz_rate, lenny_rate, hackbright_cat_1, hackbright_cat_2, estellas_cat_1, estellas_cat_2])
    db.session.commit()

    # add links between categories and businesses to reference table

    hackbright_link_1 = BusinessCategory(cat_bus_id=999, business_id=999, category_id=999)
    hackbright_link_2 = BusinessCategory(cat_bus_id=998, business_id=999, category_id=998)

    estellas_link_1 = BusinessCategory(cat_bus_id=997, business_id=998, category_id=997)
    estellas_link_2 = BusinessCategory(cat_bus_id=996, business_id=998, category_id=996)

    db.session.add_all([hackbright_link_1, hackbright_link_2, estellas_link_1, estellas_link_2])
    db.session.commit()


if __name__ == "__main__":
    # if run interactively, this will allow access of the db

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."