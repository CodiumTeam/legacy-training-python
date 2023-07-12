from urllib.request import urlopen
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
            response = json.loads(self._find_latitude_and_longitude(city))
            latitude = response['data'][0]['latitude']
            longitude = response['data'][0]['longitude']

            # Find the predictions for the location
            url = "https://api.open-meteo.com/v1/forecast?latitude="+ str(latitude) + "&longitude=" + str(longitude) + "&daily=weathercode,windspeed_10m_max&current_weather=true&timezone=Europe%2FBerlin"
            response = json.loads(urlopen(url).read().decode("utf-8"))

            for i in range(7):
                if response["daily"]['time'][i] == aDateTime.strftime('%Y-%m-%d'):
                    if (wind):
                        return response['daily']['windspeed_10m_max'][i]
                    else:
                        weatherCode = response['daily']['weathercode'][i]
                        return self.codeToText(weatherCode)

        else:
            return ""

    def _find_latitude_and_longitude(self, city):
        Request("https://api.api-ninjas.com/v1/geocoding?city=" + city)
        request.add_header("X-Api-Key", "GZmFvwGzDO1X365MONdH4A==ZCVTopwueIVfYrKN")
        return urlopen(request).read().decode("utf-8")

    def codeToText(self, weatherCode):
        return {
            0: 'Clear sky',
            1: 'Mainly clear, partly cloudy, and overcast',
            2: 'Mainly clear, partly cloudy, and overcast',
            3: 'Mainly clear, partly cloudy, and overcast',
            45: 'Fog and depositing rime fog',
            48: 'Fog and depositing rime fog',
            51: 'Drizzle: Light, moderate, and dense intensity',
            53: 'Drizzle: Light, moderate, and dense intensity',
            55: 'Drizzle: Light, moderate, and dense intensity',
            56: 'Freezing Drizzle: Light and dense intensity',
            57: 'Freezing Drizzle: Light and dense intensity',
            61: 'Rain: Slight, moderate and heavy intensity',
            63: 'Rain: Slight, moderate and heavy intensity',
            65: 'Rain: Slight, moderate and heavy intensity',
            66: 'Freezing Rain: Light and heavy intensity',
            67: 'Freezing Rain: Light and heavy intensity',
            71: 'Snow fall: Slight, moderate, and heavy intensity',
            73: 'Snow fall: Slight, moderate, and heavy intensity',
            75: 'Snow fall: Slight, moderate, and heavy intensity',
            77: 'Snow grains',
            80: 'Rain showers: Slight, moderate, and violent',
            81: 'Rain showers: Slight, moderate, and violent',
            82: 'Rain showers: Slight, moderate, and violent',
            85: 'Snow showers slight and heavy',
            86: 'Snow showers slight and heavy',
            95: 'Thunderstorm: Slight or moderate',
            96: 'Thunderstorm with slight and heavy hail',
            99: 'Thunderstorm with slight and heavy hail',
        }[weatherCode]
