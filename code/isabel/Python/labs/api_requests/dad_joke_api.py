import requests
import time

# response = requests.get('https://icanhazdadjoke.com/')
# #print(response.headers)
# data = response.json()
# print(data)

url = 'https://icanhazdadjoke.com/'

response = requests.get(url, headers ={'Accept':'application/json'})
data = response.json()
print(data['joke'])

