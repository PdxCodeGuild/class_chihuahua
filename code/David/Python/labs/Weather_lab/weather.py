import requests
import json

city = input("City: ")
state = input('State (US only): ')
country = input("Country: ")
unit_select = int(input("""
1. Freedom Units
2. Other people units

Choice:

"""))
if unit_select == 1:
    unit = 'imperial'
elif unit_select == 2:
    unit = 'metric'
limit = 1

api = '2ad9594ed07f9067be85070d97c3d641'

request_location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={api}")
location_pull = request_location.json()

# print(location_pull)

lat = location_pull[0]["lat"]
lon = location_pull[0]['lon']

# print(f'{lat} and {lon}')

weather_request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={unit}&appid={api}')
weather_pull = weather_request.json()

print(f"""
Description: {weather_pull['weather'][0]['description']}
Temperature: {weather_pull['main']['temp']}
Low:         {weather_pull['main']['temp_min']}
High:        {weather_pull['main']['temp_max']}
Feels Like:  {weather_pull['main']['feels_like']}

""")