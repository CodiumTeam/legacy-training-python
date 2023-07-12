import unittest

from tests.testable_weather import TestableWeather


class TestWeather(unittest.TestCase):

    def test_weather_prediction_for_madrid(self):
        weather = TestableWeather()

        prediction = weather.predict("Madrid")

        self.assertEqual("Mainly clear, partly cloudy, and overcast", prediction)
