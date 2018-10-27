import datetime
from weather import Weather

# find the weather of today
aWeather = Weather()
prediction = aWeather.predict('Madrid')
print('Today: ' + prediction)


# test find the weather of any day
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
aWeather = Weather()
prediction = aWeather.predict('Madrid', tomorrow)
print('Tomorrow: ' + prediction)

# test find the wind of any day
aWeather = Weather()
prediction = aWeather.predict('Madrid', None, True)
print('Wind: ' + str(prediction))


# test there is no prediction for more than 5 days
when = datetime.datetime.now() + datetime.timedelta(days=6)
aWeather = Weather()
prediction = aWeather.predict('Madrid', when)
print("Unexisting prediction " + prediction)
