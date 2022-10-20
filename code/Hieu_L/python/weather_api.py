import json
import requests
#----------- v1 displays weather
def lat_and_long(zip_code):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}&appid=884cfd64f3a52a3354c76c381207cf1e')
    data = response.json()
    return data

def current_weather(zip):
    lat = zip['lat']
    lon = zip['lon']
    response =  requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e')
    data = response.json
    weather_data = data()['main']['temp'] # need to pull specifics from this json file instead of just returning the entire file
    return weather_data


def five_day_forecast(zip):
    lat = zip['lat']
    lon = zip['lon']
    response =  requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e')
    data = response.json()
    day_one_data = data['list'][0]['main']["temp"]
    day_two_data = data['list'][1]['main']['temp']
    day_three_data = data['list'][2]['main']['temp']
    day_four_data = data['list'][3]['main']['temp']
    day_five_data = data['list'][4]['main']['temp']
    return f'day 1:{day_one_data}, \nday 2:{day_two_data}, \nday 3:{day_three_data} \nday 4:{day_four_data} \nday 5:{day_five_data}'
# zip_code = input('enter zip code: ')
# zip = lat_and_long(zip_code)
# weather = current_weather(zip)
# print(weather)


#-------------- v2 asking for specific outputs


def weather_api(choice):
    if choice == '1':
        zip_code = input('enter zip code: ')
        zip = lat_and_long(zip_code)
        weather = current_weather(zip)
        return f"the temperature out today is {weather}"
    else:
        zip_code = input('enter zip code: ')
        zip = lat_and_long(zip_code)
        weather = five_day_forecast(zip)
        return weather
choice = input('enter 1 for current weather \nenter 2 for 5 day forecast \n')
weather = weather_api(choice)
print(weather)