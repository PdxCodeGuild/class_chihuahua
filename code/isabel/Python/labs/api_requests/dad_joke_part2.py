import requests
import time

url = 'https://icanhazdadjoke.com/search'
# terms = 'hipster'

# # response = requests.get(url, headers ={'Accept':'application/json'}, params={"term":terms})

# response = requests.get(f'https://icanhazdadjoke.com/search', headers ={'Accept':'application/json'}, params={"term":terms})
# data = response.json()

# print(data)

while True:
    ask_user = input('Please enter a search word: ')
    terms = ask_user
    response = requests.get(f'https://icanhazdadjoke.com/search', headers ={'Accept':'application/json'}, params={"term":terms})
    data = response.json()
    # for i in data['results']:
    #     if data[i]['joke'].find(terms) == terms: 
    # print(data['results'][1]['joke'])
    print(f"1: {data['results'][0]['joke']}\n2: {data['results'][1]['joke']}\n3: {data['results'][2]['joke']}")
