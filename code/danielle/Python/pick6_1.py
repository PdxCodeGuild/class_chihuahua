
import random

def pick6():
    winning = []
<<<<<<< HEAD
    ticket = []
=======
    user_ticket = []
>>>>>>> 28a5ab8527a406c2de2ec6719bb2230bfeed4894
    n = 6
    for num in range(n):
        winning.append(random.randint(1,100))
<<<<<<< HEAD
    ticket = input("Choose 6 numbers (1-99), separated by a comma and space: ")
    print(f"Winning ticket: {winning} Your ticket: [{ticket}]")
   
    def num_matches(winning, ticket):
        for winning in ticket:
            if winning == ticket:
                print("Your ticket matches the winning ticket")

    num_matches(winning, ticket)

pick6()
##################################################
# Have the computer play pick6 many times and determine net balance.

# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000
# One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

# Steps
# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
=======
    for num in range(0,6):
        user = input("Choose 6 numbers, pressing enter after each selection: ")
        user_ticket.append(user)
    print(user_ticket)

    def num_matches(winning, user_ticket):
        balance = 0
        for winning in user_ticket:
            if winning == user_ticket:
                balance = balance - 2
                print(f"{balance}")
    
    num_matches(winning, user_ticket)

pick6()
>>>>>>> 28a5ab8527a406c2de2ec6719bb2230bfeed4894
