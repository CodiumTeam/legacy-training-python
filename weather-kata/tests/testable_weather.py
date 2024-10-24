import datetime

from weather import Weather


class TestableWeather(Weather):

    def _find_latitude_and_longitude(self, city):
        return '[{"name": "Madrid", "latitude": 40.4167047, "longitude": -3.7035825, "country": "ES", "state": "Community of Madrid"}, {"name": "Madrid", "latitude": 41.8766526, "longitude": -93.8232813, "country": "US", "state": "Iowa"}, {"name": "Madrid", "latitude": 4.7333686, "longitude": -74.2629794, "country": "CO"}, {"name": "Madrid", "latitude": 31.035862, "longitude": -85.39815287941555, "country": "US", "state": "Alabama"}, {"name": "Madrid", "latitude": 35.4067261, "longitude": -106.1522134, "country": "US", "state": "New Mexico"}]'

    def _find_prediction(self, latitude, longitude):
        return '{"latitude":40.43,"longitude":-3.67,"generationtime_ms":0.7439851760864258,"utc_offset_seconds":7200,"timezone":"Europe/Berlin","timezone_abbreviation":"CEST","elevation":684.0,"current_weather":{"temperature":32.8,"windspeed":19.4,"winddirection":235.0,"weathercode":3,"is_day":1,"time":"2023-07-12T15:00"},"daily_units":{"time":"iso8601","weathercode":"wmo code","windspeed_10m_max":"km/h"},"daily":{"time":["2023-07-12","2023-07-13","2023-07-14","2023-07-15","2023-07-16","2023-07-17","2023-07-18"],"weathercode":[3,3,0,0,3,2,0],"windspeed_10m_max":[20.0,14.6,22.6,27.6,17.7,9.4,14.4]}}'

    def _now(self):
        return datetime.datetime(2023,7,12)