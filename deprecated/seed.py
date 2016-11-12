# yelp_id | name | address_1 | address_2 | city | state_code | zipcode | phone | lat | long | categories
from models import Business, User, Category, BusinessCategory, Rating
from sys import argv
from models import connect_to_db, db
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

if __name__ == "__main__":
    # if run interactively, this will allow access of the db

    from server import app
    connect_to_db(app)
    print "Connected to DB."

def _add_to_businesses(params):
    """adds dictionary of attributes to businesses db"""
    print params
    if not Business.query.filter_by(yelp_id=params['yelp_id']).first():
        business = Business()
        cat_list = []
        for key in params:
            # adds elements in category lists to category table if they don't already exist
            if key == "categories":
                for cat in params[key]:
                    cat_list.append(cat)
                    if not Category.query.filter_by(category_name=cat).first():
                        category = Category(category_name=cat)
                        db.session.add(category)
                # THROUGH LINE 40 REPLACED BY 30-34
                # for group in params[key]:
                #     print type(group)
                #     for subtype in group:
                #         print type(subtype)
                #         if not Category.query.filter_by(category_name=subtype).first():
                #             category = Category(category_name=subtype)
                #             db.session.add(category)
                #         cat_list.append(subtype)
                #         print cat_list
            elif key == "yelp_id":
                business.yelp_id = params[key]
            elif key == "name":
                business.name = params[key]
            elif key == "address_line_1":
                business.address_line_1 = params[key]
            elif key == "address_line_2":
                business.address_line_2 = params[key]
            elif key == "city":
                business.city = params[key]
            elif key == "state":
                business.state = params[key]
            elif key == "zipcode":
                business.zipcode = params[key]
            elif key == "phone":
                business.phone = params[key]
            elif key == "latitude":
                business.latitude = params[key]
            elif key == "longitude":
                business.longitude = params[key]
        try:
            db.session.add(business)
            db.session.commit()
        except:
            db.session.rollback()
            print business.name, "has insufficient information, skipping."
            return None
    # creates rows in reference table
        for cat in cat_list:
            # creates row in reference table
            business = Business.query.filter_by(yelp_id=params['yelp_id']).first()
            catbus = BusinessCategory()
            print business.business_id
            catbus.business_id = business.business_id
            cat_object = Category.query.filter_by(category_name=cat).first()
            print cat_object.category_name
            catbus.category_id = cat_object.category_id

            if not BusinessCategory.query.filter_by(business_id=catbus.business_id,
                                                     category_id=catbus.category_id).first():
                db.session.add(catbus)
        db.session.commit()

        print "added " + business.name + " to db"

    else:
        print "Already in Dictionary"
        return None


def seed_user(filename):
    """seeds and adds user to db"""
    linecount = 0
    f = open(filename)
    for row in f:
        type(row)
        row = row.rstrip()
        row = row.split("|")
        print linecount
        if len(row) >= 3:
            if not User.query.filter_by(email=row[1]).first():
                user = User(name=row[0], email=row[1], password=row[2])
                try:
                    db.session.add(user)
                    db.session.commit()
                except:
                    db.session.rollback()
                    print user.name, "has insufficient information, skipping."
                linecount += 1
                print "added user", linecount
            else:
                print "user already exists"

    print "Complete.", linecount, "users added"
    f.close()


def seed_rating(filename):
    linecount = 0
    f = open(filename)
    for row in f:
        row = row.rstrip()
        row = row.split("|")
        print linecount
        time = datetime.now()
        print time
        if not Rating.query.filter_by(user_id=row[0], business_id=row[1]).first():
            rating = Rating(user_id=row[0], business_id=row[1], score=row[2], created_at=time)
            if row[3] != '':
                rating.review = row[3]
            else:
                pass
            try:
                db.session.add(rating)
                db.session.commit()
            except:
                db.session.rollback()
                print "is borked."
            linecount += 1
            print "added", linecount
        print "complete", linecount, "ratings added"
    f.close()
def seed_yelp(filename):
    """parses file of businesses from seed-business.py"""
    print "Businesses"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    # Business.query.delete()
    linecount = 0
    f = open(filename)
    for row in f:

        row = row.rstrip()
        row = row.split("|")

        attributes = {}
        attributes['yelp_id'] = str(unicode(row[0]))
        attributes['name'] = str(unicode(row[1]))

        if row[2] != "":
            attributes ['address_line_1'] = str(row[2])

        # checks if nullable field is equal to an empty string
        if row[3] != "":
            attributes['address_line_2'] = str(row[3])
        if row[4] != "":
            attributes['city'] = str(row[4])
        if row[5] != "" and len(row[5]) == 2:
                attributes['state'] = str(row[5])
        if row[6] != "":
            attributes['zipcode'] = str(row[6])
        if row[7] != "":
            attributes['phone'] = str(row[7])
        if row[8] != "":
            attributes['latitude'] = float(row[8])
        if row[9] != "":
            attributes['longitude'] = float(row[9])
        if row[10] != "":
            elements=[]
            for element in row[10:]:
                elements.append(element)

            # attributes['categories'] = row[10]
            attributes['categories'] = elements
        # debugging
        print attributes['categories']

        linecount += 1
        print "adding line " + str(linecount)

        _add_to_businesses(attributes)

    print "Complete"
    f.close()

def santize_businesses():
    """sanitizes db of all businesses without ratings from users"""
    businesses = Business.query.filter(Business.ratings is None)
    for business in businesses:
        db.session.delete(business)
    db.session.commit()
