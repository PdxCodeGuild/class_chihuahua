import requests

user_choose_api = input('Do you want to check out the Current Weather (please type \'current\') or 3 hour 5 day forecast (please type \'forecast\')?  ')

if user_choose_api == 'current':
    user_ask_lat = input('Please enter a latitute: ')
    lat = float(user_ask_lat)
    user_ask_lon = input('Please enter a longitude: ')
    lon = float(user_ask_lon)
    response_current_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e')
    data_current = response_current_weather.json()
    print(data_current)
elif user_choose_api == 'forecast':
    user_ask_city_name = input('Please enter name of city: ')
    cityname = user_ask_city_name
    response_forecast = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={cityname}&appid=884cfd64f3a52a3354c76c381207cf1e')
    data_forecast = response_forecast.json()
    print(data_forecast)
else:
    print('Please choose \'current\' or \'forecast\'')

    
    




