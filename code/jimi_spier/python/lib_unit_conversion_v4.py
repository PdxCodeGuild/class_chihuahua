# Jimi Spier
# lib_unit_converter_v4.py
# 20220912
# ----------------------Dictionary------------------------------------------ #
converstion_dict_meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm' : 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
} #meter conversions

converstion_dict_feet = {
    'ft': 1,
    'mi': 0.000189394,
    'm' : 0.3048,
    'km': 0.0003048,
    'yd': 0.333333,
    'in': 12
} #feet conversions 

converstion_dict_mile = {
    'ft': 5280,
    'mi': 1,
    'm' : 1609.34,
    'km': 1.60934,
    'yd': 1760,
    'in': 63360
} #mile conversions

converstion_dict_kilometer = {
    'ft': 3280.84,
    'mi': 0.621371,
    'm' : 1000,
    'km': 1,
    'yd': 1093.61,
    'in': 39370.1
} #kilometer conversions

choice_dict = {
    "ft": "feet",
    "mi": "miles",
    "km": "kilometers",
    "m" : "meters"
} #dictionary of available functions

# ----------------------Math Function------------------------------------------------------- #

def conversion_math(unit_one, unit_two, distance):
    usr_distance = float(distance) #convert user_input into interger

    if unit_one == "km": #decides if kimometers and if entered correctly
        total_conv = converstion_dict_kilometer[unit_two] * usr_distance #grabs data from kilometer dict and performs math
        print(f"{distance} {choice_dict[unit_two]} converted into kilometers is: {total_conv} \n")# prints to console user data with choice spelled out

    elif unit_one == "m": #decides if meters and if entered correctly
       total_conv = converstion_dict_meters[unit_two] * usr_distance #grabs data from meters dict and performs math
       print(f"{distance} {choice_dict[unit_two]} converted into meters is: {total_conv} \n")# prints to console user data with choice spelled out

    elif unit_one == "mi": #decides if miles and if entered correctly
       total_conv = converstion_dict_mile[unit_two] * usr_distance #grabs data from mile dict and performs math
       print(f"{distance} {choice_dict[unit_two]} converted into miles is: {total_conv} \n")# prints to console user data with choice spelled out

    elif unit_one ==  "ft": #decides if feet and if entered correctly
       total_conv = converstion_dict_feet[unit_two] * usr_distance #grabs data from feet dict and performs math
       print(f"{distance} {choice_dict[unit_two]} converted into feet is: {total_conv} \n") # prints to console user data with choice spelled out

    else:
        print("Invalid entry") #if entry is not as prescribed, spits out error message
     
