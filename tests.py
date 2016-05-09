import unittest
import helper

class TestCase(unittest.TestCase):

    def test_current_lat_long(self):
        """tests lat/long function"""
        func = helper.current_lat_long()
        self.assertTrue(type(func) is tuple)
        self.assertTrue(type(func[0]) is float)
        self.assertTrue(type(func[0]) is float)


if __name__ == "__main__":
    unittest.main()