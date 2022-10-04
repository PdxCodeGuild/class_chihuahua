import requests

lat = input("What is your latitude? ")
# Can use 44.92 or 34.29 as an example
lon = input("What is your longitude? ")
# Can use -123.0 or -83.82 as an example
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e")
data = response.json()
print(data['coord'][0])