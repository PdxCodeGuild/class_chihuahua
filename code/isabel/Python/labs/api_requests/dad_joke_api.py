import requests
import time

# response = requests.get('https://icanhazdadjoke.com/')
# #print(response.headers)
# data = response.json()
# print(data)

url = 'https://icanhazdadjoke.com/'

response = requests.get(url, headers = {"HTTP_ACCEPT":'application/json'})
print(response.json())

