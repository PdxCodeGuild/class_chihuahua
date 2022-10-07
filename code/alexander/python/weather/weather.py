import requests


lat = input("what is the latitude?")
lon = input("what is the longitude?")
api_key = "884cfd64f3a52a3354c76c381207cf1e"
response =  requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
data = response.json()

print(data)

#http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API key}

#api: 884cfd64f3a52a3354c76c381207cf1e

# lat: 45.63
# lon: 122.67