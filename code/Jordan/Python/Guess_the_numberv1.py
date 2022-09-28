import random
x = random.randint(1,10)
guess = 0
attempts = guess

while guess != x:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 0 + 1
    if guess == x:
        print(f"Correct! You guessed {attempts} times.")
        break
    if attempts > 10:
        print("You've failed to guess the number after 10 tries. You've lost!")
        break
    else:
        print("Try again!")