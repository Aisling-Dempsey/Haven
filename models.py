"""Models and database functions for Haven project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
##############################################################################
# DB Models

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return "<user_id: %d, name: %s, email %s>" % (self.user_id,
                                                      self.name,
                                                      self.email)

class Business(db.Model):
    __tablename__ = "businesses"

    business_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    yelp_id = db.Column(db.String, unique=True)
    name = db.Column(db.String(100), nullable=False)
    address_line_1 = db.Column(db.String(100))
    address_line_2 = db.Column(db.String(100))
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipcode = db.Column(db.String(5))
    phone = db.Column(db.String(15))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return "<business_id: %d, name: %s>" % (self.business_id,
                                                self.name)


class Business_category(db.Model):
    __tablename__ = "business_categories"

    cat_bus_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.business_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))

    business = db.relationship("Business",
                               backref=db.backref("business_categories", order_by=cat_bus_id))
    category = db.relationship("Category",
                               backref=db.backref("business_categories", order_by=cat_bus_id))

    __table_args__ = (db.UniqueConstraint('business_id', 'category_id'),)

    def __repr__(self):
        return "<cat_bus_id: %d, business_id: %d, category_id: %d>" % (self.cat_bus_id,
                                                                       self.business_id,
                                                                       self.category_id)


class Category(db.Model):
    __tablename__ = "categories"

    category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<category_id: %d, category_name: %s>" % (self.category_id,
                                                         self.category_name)

class Rating(db.Model):
    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.business_id'))
    score = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User",
                           backref=db.backref("ratings", order_by=rating_id))
    business = db.relationship("Business",
                               backref=db.backref("ratings", order_by=rating_id))

    def __repr__(self):
        return "<rating_id: %d, user_id %d, business_id %d, score: %d>" % (self.rating_id,
                                                                           self.user_id,
                                                                           self.business_id,
                                                                           self.score)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///haven'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # if run interactively, this will allow access of the db

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."

