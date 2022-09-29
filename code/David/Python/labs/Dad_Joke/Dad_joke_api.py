import requests

url = "https://icanhazdadjoke.com/"

payload={}
headers = {'Accept': ('application/json')}

response = requests.request("GET", url, headers=headers, data=payload)
dad_joke = response.json()

print(dad_joke['joke'])