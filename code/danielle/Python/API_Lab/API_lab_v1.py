import requests

lat = input("What is your latitude? ")
# Can use 44.92 or 34.29 as an example
lon = input("What is your longitude? ")
# Can use -123.0 or -83.82 as an example
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=884cfd64f3a52a3354c76c381207cf1e")
data = response.json()
data_description = data['weather']
print(data_description)
<<<<<<< HEAD

=======
>>>>>>> 28a5ab8527a406c2de2ec6719bb2230bfeed4894
