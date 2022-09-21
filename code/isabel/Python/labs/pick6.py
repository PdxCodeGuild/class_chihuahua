import random

def main(a, b):

    net = a - b
    return net

def random_winning():


    winning_ticket = []
    while len(winning_ticket) < 6:
        winning_ticket.append(random.randint(1, 99))
    #print(winning_ticket)
    return winning_ticket
#print(random_winning()) #print(f"this is winning ticket {random_winning()}") 

def computer_random_ticket():
    computer_ticket = []
    while len(computer_ticket) < 6: 
        computer_random_pick = random.randint(1, 99)
        computer_ticket.append(computer_random_pick)
    #print(computer_ticket)
    return computer_ticket   
#print(computer_random_ticket()) #print(f"this is computer ticket {computer_random_ticket()}")

def compare_tickets():
    winner_ticket = random_winning()
    random_ticket = computer_random_ticket()
    
    count_matching = 0
    for element in winner_ticket:
        if element in random_ticket:
            if winner_ticket.index(element) == random_ticket.index(element):
                count_matching += 1
                #print(count_matching)
                return count_matching
            else:
                continue
        
#print(compare_tickets())

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
        if compare_tickets() == key and compare_tickets() != 'None':
            winnings = matching_picks[key]
            #print(f"this is how much won {winnings}")
            return winnings
        else:
            return 0
#print(gambling_problem())

def thousand_tries():
    count_tries = 0
    total_winnings = 0
    total_cost = 0
    while count_tries < 100000:
        count_tries += 1
        total_winnings += gambling_problem()
        total_cost += 2
    #print(total_winnings, total_cost, count_tries)
    return total_winnings, total_cost

#print(thousand_tries())#print(f"I want sum here: {type(thousand_tries())}")

wins_thousand_tries = thousand_tries()[0]
loss_thousand_tries = thousand_tries()[1]
print(f" Your net win is {main(wins_thousand_tries, loss_thousand_tries)} bucks")







