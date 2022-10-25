import requests
import json

def weather_API():
    def Five_Day():
        Five_Day = input("Do you want to receive the five day forecast? (Y/N): ")
        five_day_response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={44.92}&lon={-123.0}&appid=884cfd64f3a52a3354c76c381207cf1e")
        five_day_data = five_day_response.json()
        five_day_description = five_day_data['list'][2]
        if Five_Day == "Y":
            print(f"The five day forecast is: {five_day_description}")
        elif Five_Day == "N":
            print(f"No data available")

    def Current_Weather():
        Current_Weather = input("Do you want to receive the current weather? (Y/N): ")
        current_weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={44.92}&lon={-123.0}&appid=884cfd64f3a52a3354c76c381207cf1e")
        current_weather_data = current_weather_response.json()
        weather_description = current_weather_data['weather']
        if Current_Weather == "Y": 
            print(f"The current weather is: {weather_description}")
        elif Current_Weather == "N":
            Five_Day()
    Current_Weather()

weather_API()