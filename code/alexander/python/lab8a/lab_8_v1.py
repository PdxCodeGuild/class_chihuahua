# import random
import random
#generate random int between range 1,10
computer_guess = random.randint(1, 10)
#input the human guess
human_guess = int(input("guess a number between 1 and 10,' if you guess the same as the computer you win! "))

# create while loop to limit guesses to 10
number_of_guesses = 1
# if guess equal random int print correct! elif print try again!


while computer_guess != human_guess and number_of_guesses < 10:
    human_guess = int(input("guess a number between 1 and 10,' if you guess the same as the computer you win!"))
    number_of_guesses += 1
    print("try again!")
if computer_guess == human_guess:
    print("congratulations you win one million gajillion fofillion dollars \n disclaimer: there is no money")
if number_of_guesses >= 10 and human_guess != computer_guess:
    print("sorry dawg you used up all your guesses, womp womp")
# if guess < 11
# it says try again on the last iteration