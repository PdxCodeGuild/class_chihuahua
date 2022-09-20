import random

def random_winning():
    winning_ticket = []
    while len(winning_ticket) < 6:
        winning_random_numbers = random.randint(1, 99)
        winning_ticket.append(winning_random_numbers)
    return winning_ticket
print(random_winning())

def computer_random_ticket():
    computer_ticket = []
    while len(computer_ticket) < 6:
        computer_random_pick = random.randint(1, 99)
        computer_ticket.append(computer_random_pick)
    return computer_ticket
print(computer_random_ticket())

def compare_tickets():
    i = 0
    for i in range(len(random_winning())):
        if computer_random_ticket()[i] == random_winning()[i]:
            i += 1
            return i
        else:
            return 0
print(compare_tickets())

def gambling_problem():
    matching_picks = {
        1 : 4,
        2 : 7,
        3 : 100,
        4 : 50000,
        5 : 1000000,
        6 : 25000000
    }

    for key in matching_picks.keys():
        if compare_tickets() == key and compare_tickets != 0:
            winnings = matching_picks[key]
            print(f"this is how much won {winnings}")
            return winnings
        else:
            return 0
print(gambling_problem())

def thousand_tries():
    count_tries = 0
    total_winnings = gambling_problem()
    while count_tries < 10:
        gambling_problem()
        count_tries += 1
        print(count_tries, gambling_problem(), compare_tickets(), computer_random_ticket())
        if gambling_problem() != 0:
            total_winnings += gambling_problem()
            print(total_winnings())
        

    return total_winnings()
    
print(thousand_tries())
