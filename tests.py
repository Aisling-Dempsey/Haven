import unittest
import helper
from server import app
from models import db, Rating, User, Business, BusinessCategory, Category
from datetime import datetime


class TestCase(unittest.TestCase):

    def test_current_loc(self):
        """tests lat/long function"""
        func = helper.current_loc()
        self.assertTrue(type(func) is dict)
        self.assertTrue(type(func['latitude']) is float)
        self.assertTrue(type(func['longitude']) is float)

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

        # Connect to test database
        connect_to_db(app)

        # Create tables and add sample data
        db.create_all()
        _example_data()

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'Aisling'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as session:
                session['user_id'] = 997



    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_get_ratings(self):
        """tests helper.get_ratings(user_id)"""
        results = helper.get_ratings(999)
        self.assertEqual(type(results), dict)
        self.assertEqual(results.keys(), ['hackbright-academy-san-francisco'])
        self.assertEqual(results['hackbright-academy-san-francisco']['business_name'],
                         'Hackbright Academy')
        self.assertEqual(results['hackbright-academy-san-francisco']['score'], 2)
        self.assertEqual(type(results['hackbright-academy-san-francisco']['created_at']), str)
        self.assertEqual(results['hackbright-academy-san-francisco']['review'], "Awesome!")

    def test_get_aggregate_rating(self):
        """tests helper.get_aggregate_rating(business)"""
        business = Business.query.get(999)
        result = helper.get_aggregate_rating(business)
        self.assertEqual(result[0], 1.5)
        self.assertEqual(result[1], 2)
        self.assertEqual(type(result), tuple)

    def test_validate_db(self):
        """tests validate_db(yelp_object, haven_model=None)"""
        yelp_object = helper.yelp_by_id('piraat-pizzeria-and-rotisserie-san-francisco-2')
        helper.validate_db(yelp_object)

        piraat = Business.query.filter_by(name="Piraat Pizzeria & Rotisserie").first()

        self.assertEqual(piraat.city, "San Francisco")
        self.assertEqual(piraat.state, "CA")
        self.assertEqual(piraat.zipcode, '94102')
        self.assertEqual(piraat.phone, '4155937771')
        self.assertEqual(piraat.address_line_1, "696 Sutter St")
        self.assertEqual(piraat.address_line_2, None)
        self.assertEqual(piraat.latitude, 37.7889385749219)
        self.assertEqual(piraat.longitude, -122.411736651251)

    # todo get help with session vars in testing

    # def test_add_rating(self):
    #         form_data = {'score': 4}
    #         helper.add_rating(form_data, 999)
    #
    #         rating = Rating.query.get(1)
    #
    #         self.assertEqual(rating.business_id, 999)
    #         self.assertEqual(rating.score, 4)
    #         self.assertEqual(rating.user_id, 997)
    #         self.assertFalse(rating.review)

    # def test_add_user(self):
    #     with self.client as c:
    #
    #             payload_1 = {'email': 'test_user@test.com',
    #                          'password': 'testpass',
    #                          'name': 'Tim'}
    #             helper.add_user(payload_1)
    #             user = User.query.filter_by(email='test_user@test.com')
    #
    #             self.assertEqual(user.name, 'Tim')
    #             self.assertEqual(user.password, 'testpass')
    #             self.assertEqual(user.email, 'test_user@test.com')
    #             self.assertEqual(session['user_name'], 'Tim')
    #             self.assertEqual(session['user_id'], user.user_id)
    #             payload_2 = {'email': 'liz@liz.com',
    #                        'password': 'liz_pass',
    #                        'name': 'Liz'}
    #             status = helper.add_user(payload_2)
    #
    #             self.assertEqual(status, "That username already exists")

    def test_yelp_generator(self):
        """tests yelp_generator(term,location, offset, sort)"""
        result = helper.yelp_generator('tacos', 'San Francisco, CA', 0, 0)
        result_1 = next(result)
        result_2 = next(result)
        result_3 = next(result)

        # fixme how to check against generator type?
        # self.assertEqual(type(result),
        self.assertEqual(type(result_1), tuple)
        self.assertEqual(type(result_1[0]), dict)
        self.assertEqual(type(result_1[1]), int)

        self.assertNotEquals(result_1, result_2)
        self.assertNotEquals(result_2, result_3)
        self.assertNotEquals(result_1, result_3)

        self.assertEqual(result_1[1], 1)
        self.assertEqual(result_2[1], 2)
        self.assertEqual(result_3[1], 3)


        self.assertIn('name', result_1[0])
        self.assertIn('id', result_2[0])
        self.assertIn('rating', result_3[0])


def _example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    Rating.query.delete()
    BusinessCategory.query.delete()
    Business.query.delete()
    Category.query.delete()
    User.query.delete()

    # Add sample businesses and users
    hackbright = Business(business_id=999, yelp_id='hackbright-academy-san-francisco',
                          name='Hackbright Academy', city='San Francisco', state='CA')
    estellas = Business(business_id=998, yelp_id='estelas-fresh-sandwiches-san-francisco',
                        name='Estella\'s', city='San Francisco', state='CA')
    # listing without yelp_id
    # piraat = Business(business_id = 997, name='Piraat', city='San Francisco', state='CA')

    liz = User(user_id=999, name='Liz', email='liz@liz.com', password='liz_pass')
    leonard = User(user_id=998, name='Leonard', email='leonard@leonard.com', password='leonard_pass')
    leslie = User(user_id=997, name='Leslie', email='leslie@leslie.com', password='leslie_pass')

    db.session.add_all([hackbright, estellas, leonard, liz, leslie])
    db.session.commit()

    # add ratings and categories

    liz_rate = Rating(rating_id=999, user_id=999, business_id=999,
                      score=2, review="Awesome!", created_at=datetime.now())
    lenny_rate_1 = Rating(rating_id=998, user_id=998, business_id=998,
                          score=0, created_at=datetime.now())

    lenny_rate_2 = Rating(rating_id=997, user_id=998, business_id=999,
                         score=1, review="Pretty good.", created_at=datetime.now())

    hackbright_cat_1 = Category(category_id=999, category_name='Vocational & Technical School')
    hackbright_cat_2 = Category(category_id=998, category_name='vocation')

    estellas_cat_1 = Category(category_id=997, category_name='Delis')
    estellas_cat_2 = Category(category_id=996, category_name='delis')

    db.session.add_all([liz_rate, lenny_rate_1, lenny_rate_2, hackbright_cat_1, hackbright_cat_2, estellas_cat_1, estellas_cat_2])
    db.session.commit()

    # add links between categories and businesses to reference table

    hackbright_link_1 = BusinessCategory(cat_bus_id=999, business_id=999, category_id=999)
    hackbright_link_2 = BusinessCategory(cat_bus_id=998, business_id=999, category_id=998)

    estellas_link_1 = BusinessCategory(cat_bus_id=997, business_id=998, category_id=997)
    estellas_link_2 = BusinessCategory(cat_bus_id=996, business_id=998, category_id=996)

    db.session.add_all([hackbright_link_1, hackbright_link_2, estellas_link_1, estellas_link_2])
    db.session.commit()

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)




if __name__ == "__main__":
    unittest.main()