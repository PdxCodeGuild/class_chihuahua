import requests

weather_choice = input("Do you want to check for the current weather or retrieve the three hour forecast?: " )
weather_choice = weather_choice.lower() #to prevent the user from typing anything in upper case and breaking code
lat = input("What is the latitude coordinates you'd like to look up?:")
lon = input("What is the longitutde coordinates you'd like to look up?:")

def weather():
    if weather_choice == "current weather":
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e')
        data = response.json()
        print(data)
# will bring the whole information that the server brings back
    else:
        response_2 = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e')
        data_2 = response_2.json()
        print(data_2)
# will bring the whole information that the server brings back
print(weather())
