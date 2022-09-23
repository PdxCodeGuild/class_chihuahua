import random

# function to create the winning numbers
def pick6():
    winning_numbers = []
    n = 6
    for x in range(n):
        winning_numbers.append(random.randint(1,99))
    return winning_numbers



# # function that is supposed to generate a ticket to comparing winning ticket to.
# how much we've won
def num_matches(winning, ticket):
    total_won = 0
    matches = 0
    earnings = {
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:100000,
    6:25000000
    }
    for n in range(len(winning)):
        if winning[n] == ticket[n]:
            matches += 1
    return earnings[matches]

# loop through 100,000 times

def player_winnings():
    counter = 0
    winning_ticket = pick6()
    totals_won = 0
    while counter <= 100000:
        player_ticket = pick6()
        totals_won = totals_won + num_matches(winning_ticket, player_ticket) -2
        counter += 1
    return totals_won

print(player_winnings())

# hi alex