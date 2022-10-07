import random

x = random.randint(1, 10)
user_guess = 1000
guess = int(user_guess)
count = 0

while True:
    user_guess = input("Please type a number from 1-10: ")
    count += 1
    if guess != x:
        ask_user = input(f"You've guessed {count}.  Do you want to try again? Press y or n: ")
        if ask_user == 'y': 
            print("try again")
    continue
else:
    print("Good bye")
    


            

