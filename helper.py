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

            return ("Logged in as", db_user.name), db_user.name, db_user.user_id

        else:
            return "That password is incorrect, please try again"

    else:
        return "That username already exists"
# todo fail quick


def add_user(payload, session=session):
    """Takes form information as a dictionary and creates user account if it doesn't already exist"""
    # import pdb; pdb.set_trace()
    email = payload['email']
    password = payload['password']
    name = payload['name']

    if not User.query.filter_by(email=email).first():
        user = User(email=email, name=name, password=password)
        db.session.add(user)
        db.session.commit()
        user_id = user.user_id
        user_name = user.name
        return user_id, user_name

    else:
        return "That user already exists"


def get_ratings(user_id):
    """returns a dictionary of all of users ratings with sub-dicts of info about the ratings under the yelp_id"""
    ratings = User.query.get(user_id).ratings
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


def yelp_by_id(yelp_id):
    """returns a dictionary of yelp information using the Yelp ID"""
    return yelp_api.business_query(id=yelp_id)


def get_aggregate_rating(business):
    """takes business model and returns aggregate score and number of ratings as a tuple"""

    haven_ratings = business.ratings

    scores = [rating.score for rating in haven_ratings]
    total_score = sum(scores)
    score_count = len(scores)
    # no need for check for 0 because nothing exists in db without a rating.
    # if score_count == 0:
    return round(total_score / float(score_count), 2), score_count


def validate_db(yelp_object, haven_model=None):
    """takes the result of a yelp query by businesses id and compares it to the database entry. If any information
     on the local db is out of date, it is updated accordingly. Will also create new db if the haven_model is none"""
    print "yelp object in validate_db:", yelp_object
    print "haven_model in validate_db", haven_model
    new = False

    if haven_model is None:
        haven_model = Business()
        haven_model.yelp_id = yelp_object['id']
        new = True

    haven_model.name = yelp_object['name']

    if yelp_object['location'].get('address'):
        if len(yelp_object['location']['address']) > 1:
            haven_model.address_line_2 = yelp_object['location']['address'][1]

        haven_model.address_line_1 = yelp_object['location']['address'][0]

    # nothing in local db should not have a city and state code but if for some reason yelp wiped them, it prevents it
    # from being cleared, protecting db integrity
    if yelp_object['location'].get('city'):
        haven_model.city = yelp_object['location']['city']

    if yelp_object['location'].get('state_code'):
        haven_model.state = yelp_object['location']['state_code']

    if yelp_object['location'].get('postal_code'):
        haven_model.zipcode = yelp_object['location']['postal_code']

    if yelp_object.get('phone'):
        haven_model.phone = yelp_object['phone']

    if yelp_object['location'].get('coordinate'):
        haven_model.latitude = yelp_object['location']['coordinate']['latitude']
        haven_model.longitude = yelp_object['location']['coordinate']['longitude']
    try:
        if new:
            db.session.add(haven_model)
            print "successfully added"
        db.session.commit()
        print 'successfully committed'
        print "committed business:", haven_model


    except:
        print 'ut-oh'


def yelp_generator(term, location, offset, sort):
    """returns a generator of yelp results"""
    results = yelp_api.search_query(term=term, location=location, offset=offset, sort=sort)
    while offset < results['total']:
        for result in results['businesses']:
            offset += 1
            yield result, offset
        results = yelp_api.search_query(term=term, location=location, offset=offset, sort=sort)


def build_results(term, location, offset, sort, cutoff):
    """takes search term, location (in city, state format) and offset, sort method, and cutoff point.
        returns a tuple in the format (term, offset, company_info, sort, cutoff) where
        company_info is a dict}
    """
    result = yelp_generator(term, location, offset, sort)
    # loops through the displayed businesses and gives each one a sub dict with a key of the yelp id
    # while there are less than 10 results with an entry in the local db, loops through results and adds
    # any businesses with a haven review to a list by yelp_ids.
    company_info = {}
    # tries to build dict of 10 businesses, if less than 10, outputs available businesses.

    while len(company_info) < 10:
        # print "\n"
        # print "cutoff:", cutoff
        # print "cutoff type:", type(cutoff)
        try:
            next_up = next(result)
        except StopIteration:
            break
        # print next_up
        company = next_up[0]
        # yelp_id = company['id']
        offset = next_up[1]
        # debug console printing
        print "\n"
        print "looping through", offset
        # feeds
        entry = build_query_result(company)
        business = Business.query.filter_by(yelp_id=entry.keys()[0]).first()
        yelp_id = entry.keys()[0]
        print 'cutoff', cutoff
        # checks if there is a cutoff and outputs results with local scores above cutoff.
        if cutoff is not None:   #this doesn't work if you don't state "is not None"
            print 'got past cutoff if'
            if business:
                # print business()
                ratings = get_aggregate_rating(business)
                print "score: ", ratings[0]
                print 'name:', business.name
                score = ratings[0] + 2
                adjusted_cutoff = cutoff +2
                # uses adusted score and cutoff to allow for less than comparison with non-negative nums
                if score < adjusted_cutoff:

                    print 'rating:', ratings[0]
                    print 'cutoff:', cutoff
                    print "rating too low, skipping"
                    continue

                else:
                    print "added to company info"
                    company_info[yelp_id] = entry[yelp_id]
                    company_info[yelp_id]['score'] = score
                    company_info[yelp_id]['total_ratings'] = ratings[1]
                    print len(company_info)
                    print company_info
            else:
                continue

        # for queries with no cutoff, shows local ratings
        elif business:
            print "triggered elif"
            company_info[yelp_id] = entry[entry.keys()[0]]
            ratings = get_aggregate_rating(business)
            company_info[yelp_id]['score'] = ratings[0]
            company_info[yelp_id]['total_ratings'] = ratings[1]

        # for queries with no cutoff and no local ratings, just shows base information
        else:
            print "no cutoff, displaying everything"
            company_info[yelp_id] = entry[entry.keys()[0]]
            print 'name:', company_info[yelp_id]['name']
            print len(company_info)

    return term, offset, company_info, sort


def build_query_result(company):
    """takes result of yelp query and returns dict of attributes for display"""
    name = company['name']
    categories = ", ".join([category[0] for category in company['categories']])
    yelp_rating = company['rating']
    yelp_id = company['id']

    business_info = {yelp_id: {'yelp_score': yelp_rating,
                               'name': name,
                               'categories': categories}}
    if company.get('image_url'):
        business_info[yelp_id]['photo'] = company['image_url']

    if company['location'].get('address'):
        business_info[yelp_id]['address_line_1'] = company['location']['address'][0]
        if len(company['location']['address']) > 1:
            business_info[yelp_id]['address_line_2'] = company['location']['address'][1]

    if company['location'].get('coordinate'):
        business_info[yelp_id]['longitude'] = company['location']['coordinate']['longitude']
        business_info[yelp_id]['latitude'] = company['location']['coordinate']['latitude']
    return business_info


def add_rating(form_data, yelp_id, user_id):
    """adds a rating form data and business_id"""
    print 'yelp_id in add_rating:', yelp_id
    if Business.query.filter_by(yelp_id=yelp_id).first() is None:
        validate_db(yelp_by_id(yelp_id))
    score = int(form_data.get("score"))
    review = form_data.get("review")
    created_at = datetime.now()
    business = Business.query.filter_by(yelp_id=yelp_id).first()
    print 'business in add_rating:', business
    business_id = business.business_id
    rating = Rating(business_id=business_id,
                    user_id=user_id,
                    score=score,
                    created_at=created_at)
    if review:
        rating.review = review

    db.session.add(rating)
    db.session.commit()

    return "Your rating has been added!"


def most_recent_review(business):
    """takes Business model from local db and returns a tuple of the most recent score with a written review, or
     if there are no written reviews, a tuple with the most recent score and None"""
    business.ratings.reverse()
    for rating in business.ratings:
        if rating.review:
            return rating.score, rating.review
        else:
            pass
    #     if no written review, returns most recent score
    return business.ratings[0].score, None


def get_business_ratings(business_id):
    """returns list of business rating models for business_id"""
    business = Business.query.filter_by(yelp_id=business_id).first()
    return business.ratings


def best_local_business(location, cutoff, term=None):
    offset = 0
    result = yelp_generator(term, location, offset, 1)
    best_businesses = {}
    while True:
        try:
            # fixme Traceback (most recent call last):
            # File "<stdin>", line 1, in <module>
            #  File "helper.py", line 310, in best_local_business
            #      yelp_business = (next(result))[0]
            #     TypeError: dict object is not an iterator

            print '/n'
            print 'type result:', type(result)
            next_up = (next(result))
            print 'type next_up:', type(next_up)
            yelp_business = next_up[0]
            print "offset:", next_up[1]
            print type(yelp_business)
            print 'yelp_business:', yelp_business
            yelp_id = yelp_business['id']
            print 'yelp_id:', yelp_id
            business = Business.query.filter_by(yelp_id=yelp_id).first()
            print business
            if business:
                score = get_aggregate_rating(business)
                print 'score:', score
                print 'cutoff:', cutoff
                if (score[0]+2) > cutoff:
                    print 'calling build_query'
                    business_info = build_query_result(yelp_business)
                else:
                    continue
            else:
                continue

            best_businesses[yelp_business['id']] = business_info[yelp_id]
        except StopIteration:
            print '\n'
            print 'end reached, businesses:', best_businesses
            return best_businesses



if __name__ == "__main__":
    # if run interactively, this will allow access of the db

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."


###########################
# deprecated code
###########################

# def add_business(info):
#     """adds business to local db along with categories from a dictionary of yelp query results"""
#     business = Business()
#
#     # for search, add key ['businesses'] before these keys
#
#     business.yelp_id = info['id']
#     business.name = info['name']
#     address = info['location'].get('address')
#     # checks for an address and adds all applicable lines to information dictionary
#     if address:
#         business.address_line_1 = address[0]
#         if len(address) > 1:
#             business.address_line_2 = address[1]
#
#     business.city = info['location']['city']
#     business.state = info['location']['state_code']
#     business.zipcode = info['location']['postal_code']
#
#     if info.get('phone'):
#         business.phone = info['phone']
#
#     # checks for coordinates and adds them to information dictionary if they exist
#     coordinates = info['location'].get('coordinate')
#     if coordinates:
#         business.latitude = coordinates['latitude']
#         business.longitude = coordinates['longitude']
#
#     # empty list of categories
#     cat_list = []
#
#     categories = info.get('categories')
#     if categories:
#         for group in categories:
#             for category in group:
#                 if not Category.query.filter_by(category_name=category).first():
#                     cat_list.append(category)
#                     category = Category()
#                     db.session.add(category)
#             db.session.commit()
#
#     # adds categories and business id to reference tables
#     for cat in cat_list:
#         # creates row in reference table
#         catbus = BusinessCategory()
#
#         catbus.business_id = business.business_id
#         cat_object = Category.query.filter_by(category_name=cat).first()
#         catbus.category_id = cat_object.category_id
#
#         if not BusinessCategory.query.filter_by(business_id=catbus.business_id, category_id=catbus.category_id):
#             db.session.add(catbus)
#     db.session.commit()
#
#
#     # temporary debug
#     db.session.add(business)
#     db.session.commit()
#
#
# def find_bus_id(id_to_check):
#     """validates whether an ID is a business_id or a yelp_id and returns the business_id"""
#
#     try:
#         return int(id_to_check)
#     except ValueError:
#         result = Business.query.filter_by(yelp_id=id_to_check).first()
#         return result.business_id
