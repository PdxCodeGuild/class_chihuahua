from multiprocessing.connection import answer_challenge
import random

x = random.randint(1,10)
print(x)

guess = input("guess the number: ")
# guess = []
# counts = enumerate(guess)
tally = []
tally = int(tally)
while guess != x and < 10:

    print(guess)
    if guess!= x:
        tally += 1
    if tally == 10:
        print('you failed 10 times')

        print("try again!")
        print(x)
        continue
    # else:
    #     print("correct! you guessed it")  
    #     break  

#     counts = enumerate(guess)
#     if guess == x:
#         print(f"correct? you guessed {counts} times")
# print try_again 9 times in a while loop unless they guess the answer_challenge
# how do you count that?
