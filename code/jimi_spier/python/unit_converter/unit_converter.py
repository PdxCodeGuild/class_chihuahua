# Jimi Spier
# unit_converter.py
# 20220908

# ----------------------Dictionary------------------------------------------------- #
conversion_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm' : 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
} #dictionary to hold values

# ----------------------User-Data-Collect------------------------------------------ #


print("Here are your options:") # Options
for key in conversion_dict: #Enumerate units on screen vertically
    print(key)

user_units = input("What unit do you want to convert into meters: ") #grabs user input for units to convert to meters
user_input = input("what is the distance:? ") #grabs user input for distance to convert to meters
print() # space
# ----------------------Math------------------------------------------------------- #
user_input = int(user_input) #convert user_input into interger
user_unit_choice = conversion_dict[user_units] #grab dictionary value and move it to unit_user_choice
conversion = 0.0 # setting up conversion as a float
conversion = user_input * user_unit_choice # perform math and dump value in conversion
rnd_conversion = round(conversion, 4) # rounding conversion with four decimal places

# ----------------------Final-Result------------------------------------------------ #
print(f'{user_input} {user_units} is {rnd_conversion}m \n') # outputs user's order on screen