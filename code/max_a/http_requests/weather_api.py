import requests

longitude = input("Enter city longitude: ")
latitude = input("Enter city latitude: ")
choice = input("Air Pollution (AP) or Current Weather (CW): ")
apik = "884cfd64f3a52a" + "3354c76c381207cf1e"

aqi_values = {
    1: "Good",
    2: "Fair",
    3: "Moderate",
    4: "Poor",
    5: "Very Poor"
}

if choice == "AP":
    response = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={latitude}&lon={longitude}&appid={apik}')
    data = response.json()
    aqi = data["list"][0]["main"]["aqi"]
    carbon_dioxide = data["list"][0]["components"]["co"]

    print(f"Air Pollution for {longitude}, {latitude}:")
    print(f"Air Quality Index: {aqi_values[aqi]}")
    print(f"Carbon Dioxide Concentration: {carbon_dioxide} micrograms per cubic meter")
    
elif choice == "CW":
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={apik}')
    data = response.json()
    weather_desc = data["weather"][0]["description"]
    city_name = data["name"]
    temperature = data["main"]["temp"]

    print(f"Current Weather for {city_name}:")
    print(f"Conditions: {weather_desc}")
    print(f"Temperature: {temperature - 273.15} degrees Celcius")