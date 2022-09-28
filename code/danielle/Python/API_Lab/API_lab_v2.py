import requests

def weather_API():
    lat = input("What is your latitude? ")
# Can use 44.92 or 34.29 as an example
    lon = input("What is your longitude? ")
# Can use -123.0 or -83.82 as an example
    Current_Weather = input("Do you want to receive the current weather? (Y/N): ")
    current_weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e")
    current_weather_data = current_weather_response.json()
    Five_Day = input("Do you want to receive the five day forecast? (Y/N): ")
    five_day_response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e")
    five_day_data = five_day_response.json()
    if Current_Weather == "Y": 
        print(f"The current weather is: {current_weather_data}")
    elif Current_Weather == "N":
        print(Five_Day)
    if Five_Day == "Y":
        print(f"The five day forecast is: {five_day_data}")
    elif Five_Day == "N":
        print(f"No data available")

weather_API()

