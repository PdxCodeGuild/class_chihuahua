import requests
# response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=884cfd64f3a52a3354c76c381207cf1e')
# response1  = requests.get("http://api.openweathermap.org/data/2.5/air_pollution?lat=51.485927&lon=0.24995&appid=884cfd64f3a52a3354c76c381207cf1e")
# #must ask the user for  latitude, longitude or city
lat = float(input('What is the latitude?:'))
long = float(input('What is the longitude?:'))

Five_Day_3_Hour=requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid=884cfd64f3a52a3354c76c381207cf1e')

#current weather
weather_temp=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=884cfd64f3a52a3354c76c381207cf1e")
# f''https://api.openweathermap.org/data/2.5/weather?lat={}lon={}')
# data=response.json()
# data1=response1.json()
# question1=input("")
# print(data)
# print(data1)
five_day=Five_Day_3_Hour.json()
forcast=weather_temp.json()
Current_Weather=input("Do you want to check for the Current Weather or 3-hour Forcast 5 days?: ")
if Current_Weather=='weather':
    print(forcast.get('main')) 
if Current_Weather=='5 day':
    print(five_day)  
