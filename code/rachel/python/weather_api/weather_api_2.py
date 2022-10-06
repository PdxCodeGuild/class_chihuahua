# import the request module
import requests

# ask user what city, state, and country they would like weather information for.
city_name = input("What is the city name? ")
state_code = input("What is the state? ")
country_code = input("What is the country? ")

# ask user if they would like just the current weather or more extensive forecast.
forecast_type = input("Would you like the current weather (current) or the 3 hour 5 day forecast (future)? ")

# Set up a conditional for if the user selects 'current' 
if forecast_type == "current":
    # request the weather information for the requested city, state, country and specify the units the information should be returned in.
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid=884cfd64f3a52a3354c76c381207cf1e&units=imperial')
    # initialize variable 'current' to hold the data returned from the API and request response in json.
    current = response.json()
    # pull just the temperature from the API for the requested location.
    print(f"\nCurrently, in {city_name}, {state_code} it is {current['main']['temp']} degrees fahrenheit with a high of {current['main']['temp_max']} degrees expected today.")
# if the user does not select 'current, 
else:
    # request the weather information for the city, state, and country requested from the OpenWeather API.
    response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name},{state_code},{country_code}&appid=884cfd64f3a52a3354c76c381207cf1e&units=imperial')
    # initialize variable 'forecast' to hold the data returned from the API and request response in JSON
    future = response.json()
    # initialize variable 'weather_list' to store the list of dictionaries in 'future'
    weather_list = future['list']
    # use a for loop to iterate through the dictionary and display the date/time and temperature at 3 hour intervals for 5 days.
    for weather in weather_list:
        print(f"\ndate/time: {weather['dt_txt']} -- temp: {weather['main']['temp']}")
   

