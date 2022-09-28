import requests
import time

url = 'https://icanhazdadjoke.com/'
terms = 'hipster'

response = requests.get(url, params={"search_term":"{terms}"}, headers ={'Accept':'application/json'})
# data = response.json()
# print(data)
# response = requests.get(f'https://icanhazdadjoke.com/?search_term={terms}', headers ={'Accept':'application/json'})
data = response.json()


print(data)

for word in data['joke']:
    if word == terms:
        print(data['joke'])
