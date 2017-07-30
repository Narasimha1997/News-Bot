import pyowm

def get_weather(location):
    weater_api=pyowm.OWM(API_key='48e9c8cf7215d8de20a3ecc9fe1648dc')
    forecast=weater_api.weather_at_place(location)
    forecast=forecast.get_weather()
    w=forecast.get_wind()
    h=forecast.get_humidity()
    t=forecast.get_temperature('celsius')
    forecast=weater_api.daily_forecast(location)
    tomorrow = pyowm.timeutils.tomorrow()
    s=forecast.will_be_sunny_at(tomorrow)
    predict_string=""
    if s is False:
        predict_string="And, It might rain tomorrow"
    else:
        predict_string="And, It might be sunny tomorrow"
    temp_string="Weather Report:\nTemperature: (in celsius) \n----\nCurrent:"+str(t['temp'])+'\tMinimun: '+str(t['temp_min'])+'\tMaximum: '+str(t['temp_max'])
    hum_String="\nHumidity: "+str(h)
    wind_string="\nWind\n----\nSpeed: "+str(w['speed'])+'\tDegree: '+str(w['deg'])+'\n'+predict_string
    main_string=temp_string+hum_String+wind_string
    return main_string
