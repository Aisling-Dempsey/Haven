"""Models and database functions for Haven project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
##############################################################################
# DB Models

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(15), nullable=False)


class Business(db.Model):
    __tablename__ = "businesses"

    business_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    yelp_id = db.Column(db.String, unique=True)
    name = db.Column(db.String(50), nullable=False)
    address_line_1 = db.Column(db.String(30), nullable=False)
    address_line_2 = db.Column(db.String(30))
    city = db.Column(db.String(20), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)



class Rating(db.Model):
    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.business_id'))
    score = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", backref=db.backref("ratings", order_by=rating_id))
    business = db.relationship("Business", backref=db.backref("ratings", order_by=rating_id))



##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///haven'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # if run interactively, this will allow access of the db

    from server import app
    connect_to_db(app)
    print "Connected to DB."