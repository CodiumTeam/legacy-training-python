import datetime
from weather.weather import Weather

def test_find_the_weather_of_today():
    aWeather = Weather()
    prediction = aWeather.predict('Madrid')
    print('Today: ' + prediction)


def test_find_the_weather_of_any_day():
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    aWeather = Weather()
    prediction = aWeather.predict('Madrid', tomorrow)
    print('Tomorrow: ' + prediction)

def test_find_the_wind_of_any_day():
    aWeather = Weather()
    prediction = aWeather.predict('Madrid', None, True)
    print('Wind: ' + str(prediction))


def test_there_is_no_prediction_for_more_than_5_days():
    when = datetime.datetime.now() + datetime.timedelta(days=6)
    aWeather = Weather()
    prediction = aWeather.predict('Madrid', when)
    assert "" == prediction
