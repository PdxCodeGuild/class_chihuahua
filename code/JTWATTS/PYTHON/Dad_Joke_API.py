import requests
response = requests.get('https://icanhazdadjoke.com/',
#to receive the accept application portion of the headers
headers={'Accept':'application/json'})
# print(response.headers)
#to format the data into json format
joke=response.json()
#to retreive the dictionary value of joke
print(joke.get('joke'))
# print(response.json())
# print(response)
# json_response=response.json()
# print(json_response)