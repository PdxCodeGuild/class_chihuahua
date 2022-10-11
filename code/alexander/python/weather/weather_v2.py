import requests


lat = input("what is the latitude? ")
lon = input("what is the longitude? ")
api_key = "884cfd64f3a52a3354c76c381207cf1e"

def air_pollution():
    response = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}')
    data = response.json()
    print(f"aqi = {data['list'][0]['main']['aqi']}")
def wind_speed():
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
    data = response.json()
    print(f"wind speed = {data['wind']['speed']}")

def choose():
    inp = input("would you like to know the current weather or the level of air pollution?\nchoose 1 for current wind speed\nchoose 2 for the air pollution level\n")
    if inp == "1":
        return wind_speed()
    elif inp == "2":
        return air_pollution()
        # whatevercodeyouwant_2()
    else:
        print("You must choose between 1 or 2")
        return choose()
choose()
#api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}

#api: 884cfd64f3a52a3354c76c381207cf1e

# lat: 45.63
# lon: 122.67