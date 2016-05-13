import requests
from models import Business, Rating, User, Category, Business_category
from yelpapi import YelpAPI
from flask import session, request
import os
from datetime import datetime
from models import connect_to_db, db


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
    email = payload['email']
    password = payload['password']
    db_user = User.query.filter_by(email=email).first()
    if db_user:
        if password == db_user.password:
            # todo check if correct way to store session values, currently pseudocode
            session['user'] = User.query.filter_by(email=email)
            return "Logged in as", db_user.name
        else:
            return "That password is incorrect, please try again"

    else:
        return "That username does not exist"





def current_lat_long():
    """outputs current lat/long estimate as a tuple based upon user ip"""
    r = requests.get("http://freegeoip.net/json/")
    location = r.json()
    return (location['latitude'], location['longitude'])


def yelp_by_id(yelp_ID):
    """returns a dictionary of yelp information using the Yelp ID"""
    return yelp_api.business_query(id=yelp_ID)



def add_rating(info):
    """adds rating to business from payload of logged in user_id, (non_yelp)business_id, score, and review """
    rating = Rating(user_id=info['user_id'], business_id=info['business_id'], score=info['score'])
    if info.get('review'):
        rating.review = info['review']
    db.session.add(rating)
    db.session.commit(rating)


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


def add_rating(form_data, business):
    """adds a rating form data and business_id"""
#     todo add form data fields
    user_id = session['user_id']
    business_id = find_bus_id(business)
    score = int(form_data.get("score"))
    review = form_data.get("review")
    created_at = datetime.now()

    rating = Business(business_id=business_id,
                      user_id=user_id,
                      score=score,
                      review=review,
                      created_at=created_at)

    db.session.add(rating)
    db.session.commit()




    #
    #
    #
    # return {'yelp id': yelp_id,
    #         'name': name,
    #         'Address line 1': address_line_1,
    #         'Address line 2': address_line_2,
    #         'City': city,
    #         'Zip': zipcode,
    #         'phone': phone,
    #         'latitude': latitude,
    #         'longitude': longitude}
    #
