import random

win_number = random.randint(1,11)
print(win_number)


many_tries = 0
while True:
    guess = int(input('Guess the number? '))
    if guess == win_number:
        many_tries += 1
        print(f'Congrats you guess the number: {win_number} in {many_tries} tries')
        break
    elif guess != win_number:
        print("Try Again!")
        many_tries += 1
        continue