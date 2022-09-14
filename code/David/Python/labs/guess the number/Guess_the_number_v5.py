from calendar import c
import random

win_number = 0

while True:
    num = int(input('Please select a number from 1 to 10: '))
    win_number = num
    if num > 10:
        print("Please select a smaller number")
        continue
    elif num <= 0:
        print("Come on, pick a real number")
        continue
    else:
        break

guess = 0

while guess != win_number:
    computer_guess = random.randint(1,10)
    guess = computer_guess
    if computer_guess == win_number:
        print("Looks like the computer guessed the correct number!")
        break
    else:
        print(f'The computer guessed {computer_guess} and that is incorrect')
        continue