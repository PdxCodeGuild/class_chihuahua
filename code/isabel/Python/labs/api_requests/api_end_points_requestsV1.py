import requests
user_ask_lat = input("Howdy, please provide a latitude of where you want to find air pollution data: ")
lat = float(user_ask_lat)
user_ask_long = input("Please provide a longitude of where you want to find air pollution data: ")
lon = float(user_ask_long)

response = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e')
data =  response.json()


data =  response.json()
print(data)