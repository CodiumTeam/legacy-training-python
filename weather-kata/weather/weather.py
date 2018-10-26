import urllib.request
import json
import datetime

class Weather:

    def predict(self, city, aDateTime = None, wind = False):
        # When date is not provided we look for the current prediction
        if aDateTime is None:
            aDateTime = datetime.datetime.now()
        # If there are predictions
        if (aDateTime < (datetime.datetime.now() + datetime.timedelta(days=6)).replace(hour=0, minute=0, second=0)):
            # Find the id of the city on metawheather
            woeid = json.loads(urllib.request.urlopen(
                "https://www.metaweather.com/api/location/search/?query=" + city).read())[0]['woeid']

            # Find the predictions for the city
            results = json.loads(urllib.request.urlopen(
                "https://www.metaweather.com/api/location/" + str(woeid)).read())['consolidated_weather']

            for result in results:
                # When the date is the expected
                if result['applicable_date'] == aDateTime.strftime('%Y-%m-%d'):
                    # If we have to return the wind information
                    if wind:
                        return result['wind_speed']
                    else:
                        return result['weather_state_name']
        else:
            return ""
