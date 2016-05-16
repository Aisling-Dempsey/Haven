import unittest
import helper
from server import app
from models import db, Rating, User, Business, Business_category

class TestCase(unittest.TestCase):

    def test_current_lat_long(self):
        """tests lat/long function"""
        func = helper.current_lat_long()
        self.assertTrue(type(func) is tuple)
        self.assertTrue(type(func[0]) is float)
        self.assertTrue(type(func[0]) is float)

    def test_yelp_by_id(self):
        """tests that yelp id query works"""
        func = helper.yelp_by_id('hackbright-academy-san-francisco')
        self.assertTrue(type(func) is dict)
        self.assertEqual(func['name'], 'Hackbright Academy')



class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app)

        # Create tables and add sample data
        db.create_all()
        helper.example_data()

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = True
        self.client = app.test_client()

        # unsure of verbiage in larger context. Getting an
        # off error I can't figure out when I try to run the
        # test file. get "TypeError: object of type 'bool' has no len()"
        # error when I run
        #
        with self.client as c:
            with c.session_transaction() as session:
                session['user'] = User.query.get(997)

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_add_rating(self):
            form_data = {'score': 4}
            helper.add_rating(form_data, 999)

            rating = Rating.query.get(1)

            self.assertEqual(rating.business_ID, 999)
            self.assertEqual(rating.score, 4)
            self.assertTrue(rating.user_id, 997)
            self.assertFalse(rating.review)


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    unittest.main()