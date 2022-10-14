# import the request module
import requests

# request a random joke from the icanhazdadjoke api accepting application/json headers.
response = requests.get('https://icanhazdadjoke.com', headers = { "accept": "application/json"})

# request response to be in json.
data = response.json()

# display the joke in the terminal.
print(data['joke'])