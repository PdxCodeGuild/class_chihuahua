# Version 1 
import random

number = random.randint(1, 10)
tries = 0
try_limit = 10

while tries < try_limit:
    guess = int(input("Guess the number: "))
    tries += 1
    if guess == number:
        input(f"Correct!")
        quit()
    elif tries < try_limit:
        input("Incorrect, try again!")

print(f"You used up all {try_limit} of your guesses! Game over.")
