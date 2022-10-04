import requests


def get_data():
    data= requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    response = data.json()
    data_out = response['text']
    
    return data_out



print()
print(get_data())
print()