# Version 5 
import random

number = int(input("What is your number? (I won't look): "))
tries = 0
guess = None
prev_guess = None

while True:
    if guess:
        prev_guess = guess
        prev_difference = abs(prev_guess-number)
    guess = random.randint(1, 10)
    input(f"I'm guessing it's... {guess}.")
    difference = abs(guess-number)
    tries += 1
    if guess == number:
        input(f"Correct! I guessed it in {tries} tries.")
        break
    elif guess > number:
        input("Incorrect, I should try lower!")
    else:
        input("Incorrect, I should try higher!")
    if prev_guess:
        if prev_difference > difference:
            input("(My current guess is closer than the last!)")
