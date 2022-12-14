# Jimi Spier
# weather_api_lab.py
# 20220926



# ----------------------Import------------------------------------------ #

import requests                                             # imports request module for api processing

# ----------------------Function---------------------------------------- #
def current_weather(zipcode):
    # ----------------------Data-Collect/Calls-------------------------------#
    data= requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid=884cfd64f3a52a3354c76c381207cf1e&units=imperial")
                                                            # data = gets data from site with zipcode as variable
    response = data.json()                                  # Puts response from site into json format
    
    # ----------------------Processing-------------------------------------- #

    #---------Current-Data-Storage-----------#
    data_out = response['main']["temp"]                     # Places current weather in data_out

    zip_place = response["name"]                            # Grabs City Name based off of zipcode
    
    # ----------------------Output-to-Console--------------------------------#
    return print(f"The current temp for {zip_place} is: {data_out}F\n")


# ----------------------Function---------------------------------------- #
def forcast_3hr_5day(zipcode):
    # ----------------------Data-Collect/Calls-------------------------------#
    data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?zip={zipcode},us&appid=884cfd64f3a52a3354c76c381207cf1e&units=imperial")
                                                            # data = gets data from site with zipcode as variable
    response = data.json()                                  # Puts response from site into json format
    
    # ----------------------Processing-------------------------------------- #

    #---------Five-Days-Data-Storage-----------#
    data_one = response["list"][0]['main']["temp"]          # Forecast Day One
    data_two = response["list"][1]['main']["temp"]          # Forecast Day Two
    data_three = response["list"][2]['main']["temp"]        # Forecast Day Three
    data_four = response["list"][3]['main']["temp"]         # Forecast Day Four
    data_five = response["list"][4]['main']["temp"]         # Forecast Day Five

    zip_place = response["city"]["name"]                    # Grabs City Name based off of zipcode
    # ----------------------Output-to-Console--------------------------------#
    return print(f"\nYour forecast for {zip_place} is:\nDay One  : {data_one}F\nDay Two  : {data_two}F\nDay Three: {data_three}F\nDay Four : {data_four}F\nDay Five : {data_five}F")
                                                            # returns a readable string for user


# ----------------------Function---------------------------------------- #
def user_inquiry(): 
    print()                                                 # Space for readability
    # ----------------------User-Data-Collect------------------------------- #
    choice = int(input("Enter 1 for Current Weather or 2 for 5 day Forecast: ")) #Grabs input for choice as interger
    zipcode = int(input("Enter your 5-digit zip code: "))   # Grabs input for zipcode as integer
    print() # Space for readability

    # ----------------------Processing-------------------------------------- #
    if choice == 1 and choice != 2:                         # if choice is 1 but not 2 call current_weather with zipcode inserted
        current_weather(zipcode)
    elif choice == 2 and choice != 1:                       # if choice is 2 but not 1 call forcast_3hr_5day with zipcode inserted
        forcast_3hr_5day(zipcode) 
    else:
        print("error")                                      # catch all error for when user puts in wrong data


user_inquiry()                                              # Calls function
    