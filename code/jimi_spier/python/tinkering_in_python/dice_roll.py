# Jimi Spier
# dice_roll.py
# 20220914

# ----------------------Import------------------------------------------ #

import random #imports random module to use randint() 

# ---------------------------------------------------------------------- #
user_results = [] # initialize empty list for result storage
user_number_int = 0 #initialize variable and "zero-out" memory space
while True: #keep going until manually stopped by condition
    
    # -----------------User-Data-Collect-------------------------------- #
    user_number = input("\nHow many side die to you want to cast: ") #grabs user_number from console
    
    user_number_int = int(user_number) #Converts string into interger
    # -----------------Processing--------------------------------------- #
    if user_number_int == 9999: #If 9999 is entered, break program, otherwise keep running
        break #halts program
    else: #if the user doesn't break, keep going
        dice_roll = random.randint(1, user_number_int) # inserts user_number_int into randint and stores in dice_roll
        user_results.append(dice_roll) #Appends a new result to user_results on each interation
        # -------------Final-Result-------------------------------------- #
        print(f"Your {user_number_int} sided die resulted in: {dice_roll} \n") #Gives original sided die and result
        print(f"Your results so far are: {user_results}") #Prints a tally of rolls by user
    
