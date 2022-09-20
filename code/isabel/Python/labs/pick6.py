import random

def random_winning():
    winning_ticket = []
    while len(winning_ticket) < 7:
        winning_random_numbers = random.randint(1, 99)
        winning_ticket.append(winning_random_numbers)
    return winning_ticket
print(random_winning())

def computer_random_ticket():
    computer_ticket = []
    while len(computer_ticket) < 7:
        computer_random_pick = random.int(1, 99)
        computer_ticket.append(computer_random_pick)
    return computer_ticket

def compare_tickets():
    for i in range(len(random_winning())):
        if computer_random_ticket()[i] == random_winning()[i]:
