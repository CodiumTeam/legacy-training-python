import unittest
from weather import Weather

class TestWeather(unittest.TestCase):

    def test_xxx(self):
        print(Weather().predict("Madrid"))
        self.assertEqual(True, True)