import random

# x = random.randint(1,10)

# user_guess = input("Please guess a number between 1-10 inclusive: ")
# guess = int(user_guess)
# count = 0

# while guess != x:
#     count += 1
#     if count < 10:
#         print("try again!")
#         user_guess = input("Please guess a number between 1-10 inclusive: ")
        
#     elif count == 10:
#         print("You lost")
# else:
#     print(f"You won! You had {count} tries")

x = random.randint(1,10)
print(x)

user_guess = 11
guess = int(user_guess)
count = 0

while guess != x:
    user_guess = input("Please guess a number between 1-10 inclusive: ")
    count += 1
    if count < 10:
        print("try again!")
        
        
    elif count == 10:
        print("You lost")
        
else:
    print(f"You won! You had {count} tries")