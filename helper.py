import requests
from models import Business, Rating, User
from yelpapi import YelpAPI
import os
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

def current_lat_long():
    """outputs current lat/long estimate as a tuple based upon user ip"""
    r = requests.get("http://freegeoip.net/json/")
    location = r.json()
    return (location['latitude'], location['longitude'])


def yelp_by_id(yelp_ID):
    """returns a dictionary of yelp information using the Yelp ID"""
    return yelp_api.business_query(id=yelp_ID)


def add_business(info):
    """adds business to local db by with yelp business dictionary"""
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

    business.zipcode = info['location']['postal_code']

    if info.get('phone'):
        business.phone = info['phone']

    # checks for coordinates and adds them to information dictionary if they exist
    coordinates = info['location'].get('coordinate')
    if coordinates:
        business.latitude = coordinates['latitude']
        business.longitude = coordinates['longitude']

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


def add_rating(form_data, business_id):
    """adds a rating form data and business_id"""
#     todo add form data fields



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
