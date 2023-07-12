import unittest

from weather import Weather


class TestWeather(unittest.TestCase):

    def test_weather_prediction_for_madrid(self):
        weather = Weather()

        prediction = weather.predict("Madrid")

        self.assertEqual("Mainly clear, partly cloudy, and overcast", prediction)
