'''
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance

if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000

'''

import random

jackpot = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 10000000,
    6: 25000000
}


# initialize variable to hold the value of the funds. Beginning balance is 0. 
balance = 0
#wins = 0
x = 0

# define a function that selects a list of 6 random numbers between 1 and 99. This function can be used for both the winning tickets as well the 6 numbers the user picks.
def pick_6(r, low = 1, high = 99):
    # initializes and empty list as placeholder for the random numbers
    picks = []

    # loop that will select a random number and append it to the empty list until it has looped the specified number (r) times
    for x in range(r):
        random_number = random.randint(low, high)
        picks.append(random_number)
    
    # return the randomly selected numbers
    return picks

# define a function that compares the 6 numbers on the winning ticket to the 6 numbers on the user's ticket. The function returns the number of matches.
def num_matches(winning_ticket, lotto_ticket):
   # initialized variable 'match' and set the value to 0. Every time the loop runs, match has to start out at 0 in order to count the number of matches in that loop.
   match = int(0)
    # loop will run once for each number on the ticket. It compares the numbers at the same index on the two tickets and adds 1 for each match starting at 0. Returns the number of matches including 0 if there are no matches.
   for num in range(len(winning_ticket)):
        if winning_ticket[num] == lotto_ticket[num]:
            match += 1
            return match
        else:
            return match

# define a function that returns the user's winnings, if any, and adds to their account. Every time this runs the return value is asdded to the balance with the profit_or_loss() function so this starts out at 0 every time it runs.If there are any matches between the tickets, the number of matches corresponds to a key in the jackpot dictionary and returns the value for that key.
def winner(matches):
    wins = 0
    wins += jackpot[matches]
    return wins
   
      
# initialize variable to hold the value of the player funds. Starting balance is 0. Every ticket is 2, so that must be subtracted from the balance with every loop. Any winnings will be added to the balance.
def profit_or_loss(balance, winnings):    
    balance -= 2
    balance += winnings
    return balance

# run the function to select the 6 winning numbers
winning_ticket = pick_6(6)

# use a while loop to repeat 100000 times
while x <= 100000:
    
    # this will run the pick(6) function to generate a new ticket with every loop and assigns the random numbers to new variable 'lotto_ticket'
    lotto_ticket = pick_6(6)
    # runs the num_matchesa() function that compares the winning numbers to the new ticket with every loop.
    matches = num_matches(winning_ticket, lotto_ticket) 
    # runs the winner()function that calculates whether there are any winnings with each loop.
    winnings = winner(matches) 
    # runs the profit_or_loss() function to determine the running total of funds won or lost as each loop completes, subtracting 2 for each loop and adding any winnings.
    balance = profit_or_loss(balance, winnings)
    # use x to increment the loop
    x += 1
else:
    False

print(f"Your final balance is {balance}.")