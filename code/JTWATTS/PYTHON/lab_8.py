import random    
#x is the random number
x = random.randint(1,10)
# print(x)
# we have to define guess before we can place it in our while loop
guess = 0
# we have to define tally before we can place it in our while loop.  Spent too much time trying to make a list with an interger
tally = 0
#while loop 
while guess != x and tally < 10:
    # x = random.randint(1,10)
    # print(x)
    #now that guess and tally have been defined, we can take a users input and place it in guess
    guess = int(input("guess the number: "))
    # print(tally)
    #we take each time the question is asked and add it to the tally
    tally += 1
    if guess == x:
        print(f"correct you guessed {tally}times") 
        #quit the game with break
        break
    if guess!= x:
        #no break statement because they are not done
        print("try again")
     # as stated fail 10 times and print this  
    if tally ==10:
        print('you failed 10 times')    
        #quit the game with break
        break
# print(tally)
# if tally == 10:           
#     print(x)
     

# word = "accccddeeegeelopanm"
# counted = {}
# for char in word:
#   if char in counted:
#     counted[char] += 1
#   else:
#     counted[char] = 1
# print(counted)

    # else:
    #     print("correct! you guessed it")  
    #     break  

#     counts = enumerate(guess)
#     if guess == x:
#         print(f"correct? you guessed {counts} times")
# print try_again 9 times in a while loop unless they guess the answer_challenge
# how do you count that?