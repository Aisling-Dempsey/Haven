# this method is abandoned, and only saved for posterity. use scrapebusiness.py and seed.py instead

from helper import yelp_api
from sys import argv
from models import Business, Business_category, Category, db, connect_to_db
from flask_sqlalchemy import SQLAlchemy


def build_db(city, state):

    # categories = ['active', 'arts', 'auto', 'beautysvc', 'education', 'eventservices', 'financialservices', 'food',
    #               'health', 'homeservices', 'hotelstravel', 'localflavor', 'localservices', 'massmedia', 'nightlife',
    #               'pets', 'professional', 'publicservicesgovt', 'realestate', 'religiousorgs', 'restaurants',
    #               'shopping']
    city_state= city + ", " + state
    # for category in categories:

        # result_count = yelp_api.search_query(location=city_state, category_filter=category)['total']
    result_count = yelp_api.search_query(location=city_state)['total']

    offset = 0
    added = 0
    skipped = 0
    print result_count
    # max offset is 1000
    # try:
    while offset < result_count:
        while offset < 1000:
            # print category
            # results = yelp_api.search_query(location=city_state, category_filter=category, offset=offset)
            results = yelp_api.search_query(location=city_state, offset=offset)
            for result in results['businesses']:
                try:
                    business = Business()

                    # id
                    business.yelp_id = result['id']
                    # name
                    business.name= result['name']

                    # address lines 1 and 2
                    if result['location'].get('address'):
                        business.address_line_1 = result['location']['address'][0]
                        if len(result['location']['address']) > 1:
                            business.address_line_2 = result['location']['address'][1]

                    # city
                    business.city = result['location']['city']
                    # state code
                    business.state = result['location']['state_code']
                    # zip code
                    business.zipcode = result['location']['postal_code']

                    # phone
                    if result.get('phone'):
                        business.phone = result['phone']

                    # latitude and longitude
                    if result['location'].get('coordinate'):
                        business.latitude = result['location']['coordinate']['latitude']
                        business.longitude = result['location']['coordinate']['longitude']

                    # list of categories
                    if result.get('categories'):
                        cat_list = []
                        for group in result['categories']:
                            for subtype in group:
                                if not Category.query.filter_by(category_name=subtype).first():
                                    category = Category(category_name=subtype)
                                    db.session.add(category)

                                cat_list.append(subtype)

                    # if not Business.query.filter_by(yelp_id=business.yelp_id).first():
                    #     db.session.add(business)
                    db.session.add(business)
                    db.session.commit()
                    bus_id = business.business_id

                    for cat in cat_list:
                        # creates row in reference table
                        catbus = Business_category()

                        catbus.business_id = bus_id

                        cat_object = Category.query.filter_by(category_name=cat).first()
                        catbus.category_id = cat_object.category_id

                        db.session.add(catbus)
                    db.session.commit()
                    added += 1
                    print "added" + str(added)
                    print business.name
                except:
                    print "already added:" + business.name
                    print 'skipped' + str(skipped)
                    skipped += 1
                    print "added so far: " + str(added)

                db.session.commit()
                offset += 20
    # breaks out of loop when reaches 999
    # break

    # except:
    #     pass


if __name__ == "__main__":
    # if run interactively, this will allow access of the db

    from server import app
    connect_to_db(app)
    print "Connected to DB."
sf_districts = ["castro, san francisco", "Chinatown, san francisco", "cole valley, san francisco",
                "financial district, san francisco", "fisherman's wharf, san francisco", "haight, san francisco",
                "hayes, san francisco", "mission, san francisco", "nob hill, san francisco",
                "tenderloin, san francisco", "noe valley, san francisco", "upper market, san francisco",
                "union square, san francisco", "soma, san francisco", "sunset, san francisco", "chapel, san francisco",
                "sixth street, san francisco", "richmond, san francisco", "russian hill, san francisco"]

sf_zips = [94102, 94103, 94104, 94105, 94107, 94108, 94109, 94110, 94111, 94112, 94114, 94115, 94116, 94117, 94118,
           94121, 94122, 94123, 94124, 94127, 94129, 94130, 94131, 94132, 94133, 94134, 94158]

terms = ['school', 'vocation', 'indian', 'mexican', 'italian', 'doctor', 'hospital', 'bakery', 'asian', 'japanese',
         'landmark', 'juice', 'hawaiian', 'ethiopian', 'bubble tea', 'sandwiches', 'deli', 'pizza', 'thai', 'creperies',
         'chinese', 'japanese', 'sushi', 'coffee', 'vegan', 'vegetarian', 'tacos', 'parks', 'falafel', 'food trucks',
         'chocolate', 'meats', 'vietnamese', 'senegalese', 'homeservices', 'localflavor', 'localservices', 'health',
         'gourmet', 'food', 'beautysvc']

# for district in sf_districts:
#     build_db(district)

build_db(argv[1], argv[2])
