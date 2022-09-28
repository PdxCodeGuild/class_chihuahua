import time
import requests

url = "https://icanhazdadjoke.com/" #takes us to the JSON data

payload={}
headers = {"Accept": "application/json"} # this is basically saying, we want the response back in JSON
# header is the application data which is what we want
response = requests.request("GET", url, headers=headers, data=payload)
time.sleep(3) # for comedic, punch line before the joke presents itself

data = response.json() # putting it into a prettier format
print(data["joke"]) # accessing the value of the key of joke within the dictionary object found in terminal