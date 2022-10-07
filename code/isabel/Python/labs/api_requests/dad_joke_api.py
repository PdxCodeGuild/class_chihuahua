import requests
import time

# response = requests.get('https://icanhazdadjoke.com/')
# #print(response.headers)
# data = response.json()
# print(data)

url = 'https://icanhazdadjoke.com/'

response = requests.get(url, headers ={'Accept':'application/json'})
data = response.json()
joke = data['joke']
print(joke)

for letter in range(0, len(joke)):
    print(joke[letter], end="")
    time.sleep(0.25)




