# Version 4 
import random

number = random.randint(1, 10)
tries = 0
guess = None
prev_guess = None

while True:
    if guess:
        prev_guess = guess
        prev_difference = abs(prev_guess-number)
    guess = int(input("Guess the number: "))
    difference = abs(guess-number)
    tries += 1
    if guess == number:
        input(f"Correct! You guessed it in {tries} tries.")
        break
    elif guess > number:
        input("Incorrect, try lower!")
    else:
        input("Incorrect, try higher!")
    if prev_guess:
        if prev_difference > difference:
            input("(Your current guess is closer than the last!)")
            