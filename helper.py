import requests
from models import Business, Rating, User
from yelpapi import YelpAPI
import os


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

def add_business(yelp_ID):
    """adds business to local db by with yelp object"""
    # todo add dictionary get
    if  yelp_ID != "Unknown":
        # returns as dict, no need to convert from json
        info = yelp_api.business_query(id=yelp_ID)

        # for search, add key ['businesses'] before these keys
        yelp_id = yelp_ID
        name = info['name']
        address_line_1 = info['location']['address'][0]
        address_line_2 = info['location']['address'][1]
        city = info['location']['city']
        zipcode = info['location']['postal_code']

        phone = info['phone']
        latitude = info['location']['coordinate']['latitude']
        longitude = info['location']['coordinate']['longitude']


    return {'yelp id': yelp_id,
            'name': name,
            'Address line 1': address_line_1,
            'Address line 2': address_line_2,
            'City': city,
            'Zip': zipcode,
            'phone': phone,
            'latitude': latitude,
            'longitude': longitude}

