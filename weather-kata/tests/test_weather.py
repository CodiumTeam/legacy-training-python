import datetime
import unittest

from tests.testable_weather import TestableWeather


class TestWeather(unittest.TestCase):

    def test_weather_prediction_for_madrid(self):
        weather = TestableWeather()

        prediction = weather.predict("Madrid")

        self.assertEqual("Mainly clear, partly cloudy, and overcast", prediction)

    def test_weather_prediction_with_date(self):
        weather = TestableWeather()

        prediction = weather.predict("Madrid", datetime.datetime(2023, 7, 14))

        self.assertEqual("Clear sky", prediction)

    def test_wind_prediction(self):
        weather = TestableWeather()

        prediction = weather.predict("Madrid", None, True)

        self.assertEqual(20.0, prediction)

    def test_does_not_return_any_prediction_for_a_date_too_far(self):
        weather = TestableWeather()

        prediction = weather.predict("Madrid", datetime.datetime(2023, 7, 19))

        self.assertEqual("", prediction)
