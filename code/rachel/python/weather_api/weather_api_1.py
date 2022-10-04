import requests

# ask user what city, state, and country they would like weather information for.
city_name = input("What is the city name? ")
state_code = input("What is the state? ")
country_code = input("What is the country? ")

# request the weather information for the city, state, and country requested from the OpenWeather API.
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid=884cfd64f3a52a3354c76c381207cf1e&units=imperial')

# request response in JSON
data = response.json()
 
# display the current temp and the high temp in the requested city.
print(f"Currently, in {city_name}, {state_code} it is {data['main']['temp']} degrees fahrenheit with a high of {data['main']['temp_max']} degrees expected today.")



