import random

win_number = random.randint(1,11)
print(win_number)

tries = 10
many_tries = 0
while tries > 0:
    guess = int(input('Guess the number? '))
    if guess == win_number:
        many_tries += 1
        print(f'Congrats you guess the number: {win_number} in {many_tries} tries')
        break
    elif guess != win_number:
        tries -= 1
        many_tries += 1
        if tries == 0:
            print("Sorry you you are out of tries")
            break
        print("Try Again!")
        continue