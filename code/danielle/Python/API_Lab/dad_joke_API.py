import requests

def dad_joke():
    headers = {"Accept": "application/json"}
    website = requests.get("https://icanhazdadjoke.com/", headers=headers)
    joke = website.json()
    print(joke.get("joke"))

dad_joke()