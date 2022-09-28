# Jimi Spier
# guess_the_number_vFUN.py
# 20220913

# ----------------------Import------------------------------------------ #

import random #imports random module

# ----------------------Computer Opponent------------------------------- #

user_range_one = input("Enter the smallest number: ") # grabs variable for randint(one_int,x) beginning range
user_range_two = input("Enter the largest number: ") # grabs variable for randint(x,two_int) ending range
one_int = int(user_range_one) #converts to int
two_int = int(user_range_two) #converts to int
computer_number = random.randint(one_int,two_int) # Asks random module for a random int between one_int and two_int

#print(computer_number)# uncomment for debugging

user_attempts = 0 # initialize attempt counter with zero


# ----------------------Processing-------------------------------------- #
while True:
    user_number = input(f"Please guess a number between {one_int} and {two_int}, enter 9999 to quit: ") # grabs number from user
    
    print()# adds extra space for readability
    
    user_number_int = int(user_number) # converts user_number from string to integer
    user_attempts += 1 # adds 1 to the user_attepts counter per interation 
    
    # ----------------------Decision Making------------------------------ #

    if user_number_int == computer_number:
        print(f"Your number: {user_number_int} and the random number: {computer_number} are the same! ")
        print(f"You've guessed {user_attempts} times \n")
        break # if the user guess correctly, the system reveals the secret number and how many times attempted
    
    elif user_number_int == 9999:
        print(f"Sorry to see you go, you guessed {user_attempts} times. The secret number was: {computer_number} \n")
        break #Entering 50 breaks the loop and enables user to quit and reveals secret number
    
    elif user_number_int != computer_number: 

        # ----------------------Nested If ------------------------------ #

        if user_number_int > computer_number: #nested if to check user_number_int to see if too high, inform user
            print(f"Your number of {user_number_int} is too high \n")
        else: # If not too high, then must be too low. Inform user
            print(f"Your number of {user_number_int} is too low \n")

    # ----------------------Resumes Previous If statement---------------- #

        print(f"Your answer of {user_number_int} is not the same as the computer. You've guessed {user_attempts} times \n")
        continue # if the user number and computer number are not equal, keep going
    
    else:
        print("something's gone horribly wrong \n") # "catch-all" error
