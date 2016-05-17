import requests
from models import Business, Rating, User, Category, Business_category
from yelpapi import YelpAPI
from flask import session, request
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
            # todo check if correct way to store session values, currently pseudocode
            session['user_id'] = db_user.user_id
            session['user_name'] = db_user.name

            return "Logged in as", db_user.name

        else:
            return "That password is incorrect, please try again"

    else:
        return "That username does not exist"


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


def current_loc():
    """outputs current lat/long estimate as a tuple based upon user ip"""
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

    # addd categories and business id to reference tables
    for cat in cat_list:
        # creates row in reference table
        catbus = Business_category()

        catbus.business_id = business.business_id
        cat_object = Category.query.filter_by(category_name=cat).first()
        catbus.category_id = cat_object.category_id

        if not Business_category.query.filter_by(business_id=catbus.business_id, category_id=catbus.category_id):
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


def return_business_object(business_id):
    """returns the business object using the business_id. Often paired with find_bus_id(id_to_check)"""
    return Business.query.get(business_id)


def splash_query(form_data, location, offset=0):
    """takes user input and tuple of (city, state code) and returns search"""

#     todo build me
    term = form_data['term']
    location = location[0] + ", " + location[1]
    print location
    results = yelp_api.search_query(term=term, location=location, offset=offset, limit=10)
    total_results = results['total']
    data = {}

    # loops through the displayed businesses and gives each one a sub dict with a key of the yelp id
    for result in results['businesses']:
        parent_key = result['id']
        data[parent_key] = {}
        # makes empty list for categories and appends the first element of each returned category list to it, then
        # adds them as a key/value pair in the sub-dict for the business
        cats = []
        for category in result['categories']:
            cats.append(category[0])

        data[parent_key]['categories'] = cats

        # adds address lines 1 and 2 as well as city to the sub-dict if they exist
        address = result['location'].get('address')
        if address:
            if len(address) == 2:
                address_1 = result['location']['address'][0]
                data[parent_key]['address_1'] = address_1

                address_2 = result['location']['address'][1]
                data[parent_key]['address_2'] = address_2

            elif len(address) == 1:
                address_1 = result['location']['address'][0]
                data[parent_key]['address_1'] = address_1


        city = result['location'].get('city')
        #
        # if address_1:
        #     data[parent_key]['address_1'] = address_1
        #
        # if address_2:
        #     data[parent_key]['address_2'] = address_2

        if city:
            data[parent_key]['city'] = city

        name = result.get('name')
        data[parent_key]['name'] = name

        # adds phone number to sub-dict if it exists
        phone = result.get('display_phone')
        if phone:
            data[parent_key]['phone'] = phone

        # adds yelp rating to sub-dict
        data[parent_key]['rating'] = result['rating']

        # provides average haven rating if it exists.

        try:
            haven_ratings = Business.query.filter_by(yelp_id=result['id']).first().ratings

        except:
            pass
        scores = []

        if haven_ratings:
            # todo determine why this is erroring on w/offset 40 and a term of 'tacos'
            for rating in haven_ratings:
                scores.append(rating.score)
            total_score = 0
            score_count = 0
            for score in scores:
                total_score += score
                score_count += 1

            haven_score = total_score/float(score_count)

            data[parent_key]['haven_score'] = haven_score
            data[parent_key]['haven_count'] = score_count

        # checks for photo and adds it if it exists
        photo = result.get('image_url')
        if photo:
            data[parent_key]['photo'] = photo

    return [data, offset, total_results]



def add_rating(form_data, business, user_id):
    """adds a rating form data and business_id"""
    business_id = find_bus_id(business)
    score = int(form_data.get("score"))
    review = form_data.get("review")
    created_at = datetime.now()

    rating = Rating(business_id=business_id,
                    user_id=user_id,
                    score=score,
                    review=review,
                    created_at=created_at)

    db.session.add(rating)
    db.session.commit()


def example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    Rating.query.delete()
    Business_category.query.delete()
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
    leslie= User(user_id=997, name='Leslie', email='leslie@leslie.com', password='leslie_pass')

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

    hackbright_link_1 = Business_category(cat_bus_id=999, business_id=999, category_id=999)
    hackbright_link_2 = Business_category(cat_bus_id=998, business_id=999, category_id=998)

    estellas_link_1 = Business_category(cat_bus_id=997, business_id=998, category_id=997)
    estellas_link_2 = Business_category(cat_bus_id=996, business_id=998, category_id=996)

    db.session.add_all([hackbright_link_1, hackbright_link_2, estellas_link_1, estellas_link_2])
    db.session.commit()
