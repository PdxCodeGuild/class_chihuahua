# Jimi Spier
# unit_converter.py
# 20220908

# ----------------------Dictionary Imports------------------------------------------ #
from lib_unit_conversion_v4 import choice_dict as choices  
from lib_unit_conversion_v4 import conversion_math as cm



# ----------------------User-Data-Collect------------------------------------------ #


print("Here are your options: \n") # Options
for key in choices: #Enumerate units on screen vertically
    print(key)
print() # extra line for readability
print("Type your choice exactly as it appears or quit, to quit.")

user_conv_choice_one = " " #initialize variable to start while loop
user_conv_choice_two = " " #initialize variable to start while loop

while user_conv_choice_one != "quit": # keep looping until quit is entered
    user_conv_choice_one = input("Enter first unit to convert: ")#grabs first user input for units to convert
    user_conv_choice_two = input(f"What unit do you want to convert into {user_conv_choice_one}: ") #grabs second user input for units to convert
    user_distance = input("what is the distance:? ") #grabs user input for distance to convert
    print() # space
# ----------------------Math------------------------------------------------------- #
    cm(user_conv_choice_one, user_conv_choice_two, user_distance) #call conversion_math function and return results



