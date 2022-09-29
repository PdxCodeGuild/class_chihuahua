import requests

lat = input("What is the latitude coordinates you'd like to look up?:")
lon = input("What is the longitutde coordinates you'd like to look up?:")
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e')
data = response.json()
print(data)
# will bring the whole information that the server brings back