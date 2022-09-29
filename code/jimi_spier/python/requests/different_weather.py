import requests


def get_data():
    data= requests.get("https://api.open-meteo.com/v1/forecast?latitude=44.924720&longitude=-123.009712&hourly=temperature_2m&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FLos_Angeles&past_days=3")
    response = data.json()
    data_out = response['current_weather']
    another_data = data_out["temperature"]
    
    return another_data



print()
print(get_data())
print()