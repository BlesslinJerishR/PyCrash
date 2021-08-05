import unittest
from city_country import info


class CountryTest(unittest.TestCase):

    def test_info(self):
        city_info = info('Chennai', 'Tamilnadu')
        self.assertEqual(city_info, 'Chennai, Tamilnadu')

    def test_info_pop(self):
        city_info = info('Chennai', 'Tamilnadu', 5000000)
        self.assertEqual(city_info, 'Chennai, Tamilnadu - population 5000000')


if __name__ == '__main__':
    unittest.main()
