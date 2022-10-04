import random

win_number = random.randint(1,11)
print(win_number)

last_guess = 0

many_tries = 0
while True:
    guess = int(input('Guess the number? '))
    if guess == win_number:
        many_tries += 1
        print(f'Congrats you guess the number: {win_number} in {many_tries} tries')
        break
    elif last_guess > 0:
        many_tries += 1
        if last_guess > guess:
            print('Your Previous guess was higher than your current')
            continue
        else:
            print('Your previous guess was lower than your current')
    elif guess != win_number:
        many_tries += 1
        if guess > win_number:
            print("Too High!")
            last_guess = guess
            continue
        else:
            print("Too Low!")
            last_guess = guess
            continue