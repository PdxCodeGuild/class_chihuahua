import requests
input_term = input('what kind of joke do you want to hear')
response = requests.get('https://icanhazdadjoke.com/search', headers = {'Accept' : 'application/json'}, params = {'term' : input_term})
data = response.json()
print(data)