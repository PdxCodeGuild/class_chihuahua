# Version 2 
import random

number = random.randint(1, 10)
tries = 0

while True:
    guess = int(input("Guess the number: "))
    tries += 1
    if guess == number:
        input(f"Correct! You guessed it in {tries} tries.")
        break
    else:
        input("Incorrect, try again!")
        