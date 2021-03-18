import unittest

from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
       cape_town_rsa = city_country('cape town', 'rsa')
        self.assertEqual(cape_town_rsa, 'Cape Town, RSA')

if __name__ == '__main__':
    unittest.main()
