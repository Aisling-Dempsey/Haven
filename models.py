"""Models and database functions for Haven project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
##############################################################################
# DB Models

class User(db.model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(15), nullable=False)


class Business(db.model):
    __tablename__ = "businesses"

    business_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # TODO determine if db.string needs a max length
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    # TODO determine if db.Integer can have max length
    zipcode = db.Column(db.Integer(5), nullable=False)
    phone = db.Column(db.Integer())
    # TODO lat/long nullable?
    lat_long = db.Column([db.Integer, db.Integer])


class Rating(db.model):
    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.business_id'))
    score = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500))


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
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."