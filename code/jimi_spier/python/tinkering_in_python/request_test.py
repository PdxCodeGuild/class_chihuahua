import requests


def get_data():
    data= requests.get("http://dog-api.kinduff.com/api/facts")
    response = data.json()
    data_out = response['facts']
    
    return data_out



print()
print(get_data())
print()