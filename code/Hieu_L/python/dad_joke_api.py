from wsgiref import headers
import requests
import json

response = requests.get('https://icanhazdadjoke.com', headers = {'accept':'application/json'})
data = response.json
joke = data()['joke']
print(joke)