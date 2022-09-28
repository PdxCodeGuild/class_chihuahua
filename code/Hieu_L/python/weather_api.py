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
    data = response.json()
    return data

# zip_code = input('enter zip code: ')
# zip = lat_and_long(zip_code)
# weather = current_weather(zip)
# print(weather)


#-------------- v2 asking for specific outputs

choice = input('enter 1 for current weather \nenter 2 for 3-hour forecast \n')
def three_day_forecast(zip):
    lat = zip['lat']
    lon = zip['lon']
    response =  requests.get(f'api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e')
    data = response.json()
    return data

def weather_api(choice):
    if choice == 1:
        zip_code = input('enter zip code: ')
        zip = lat_and_long(zip_code)
        weather = current_weather(zip)
        print(weather)
    elif choice == 2:
        zip_code = input('enter zip code: ')
        zip = lat_and_long(zip_code)
        weather = three_day_forecast(zip)
        print(weather)

# choice = input('enter 1 for current weather \n enter 2 for 3-hour forecast \n')
weather = weather_api(choice)
print(weather)
