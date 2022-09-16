import random

x = random.randint(1, 10)
print(x)


count = 0

while True:
    
    user_guess = input("Please type a number from 1-10: ")

    if user_guess.isdigit() == False:
        print('type a number')
    else:
        guess = int(user_guess)
        count += 1

        if guess != x:
            ask_user = input(f"You've guessed {count}.  Do you want to try again? Press y or n: ")
        
            if ask_user == "y": 
                print("try again")
    
            elif ask_user == "n":
                print("Good bye")
                break
            else:
                print('type y or n')

        if guess == x:
            ask_user = input(f"You won! You had {count} tries.  Do you want to play again? Type y or n: ")
    
            if ask_user == "y": 
                print("try again")
    
            elif ask_user == "n":
                print("Good bye")
                break
            else:
                print('type y or n')