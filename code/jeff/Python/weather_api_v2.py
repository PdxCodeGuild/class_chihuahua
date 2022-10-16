import requests

city_name = input('\nPlease enter the city name\n')
forecast_type = input("\nWhat type of forecast\n '3 day' or 'current'")

if forecast_type == 'current':
    response =  requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=884cfd64f3a52a3354c76c381207cf1e')
    data = response.json()
    print(data['main'])
elif forecast_type == '3 day':
    response =  requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid=884cfd64f3a52a3354c76c381207cf1e')
    data = response.json()
    print(data['list'][0]['main'])
else:
    print('please try again')

