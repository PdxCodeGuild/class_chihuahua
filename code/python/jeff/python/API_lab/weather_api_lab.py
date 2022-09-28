import requests

response =  requests.get('https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={884cfd64f3a52a3354c76c381207cf1e}')
data = response.json()

print(data)
