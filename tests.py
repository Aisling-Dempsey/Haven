import unittest
import helper

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


    def test_add_business(self):
        """tests adding """







def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test'
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    unittest.main()