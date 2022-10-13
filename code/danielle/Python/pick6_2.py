import random

def pick6():
    pick6 = []
    n = 6
    for i in range(n):
        pick6.append(random.randint(1,100))
    return

pick6()

def lottery():
    ticket = pick6()
    for n in range(5):
        return ticket
    winning_ticket = pick6()
    for n in range(1):
        return winning_ticket
    print(f"{ticket} and {winning_ticket}")

lottery()
    

"""
    def num_matches(winning, ticket):
        while ticket in winning:
            if ticket[0] == winning[0]:
                print("You have 1 match")
            elif ticket[0, 1] == winning[0, 1]:
                print("You have 2 matches")
            elif ticket[0, 1, 2] == winning[0, 1, 2]:
                print("You have 3 matches")
            elif ticket[0, 1, 2, 3] == winning[0, 1, 2, 3]:
                print("You have 4 matches")
            elif ticket[0, 1, 2, 3, 4] == winning[0, 1, 2, 3, 4]:
                print("You have 5 matches")   
            elif winning == ticket:
                print("Your ticket matches the winning ticket")
    
        num_matches(winning, ticket)

pick6()
"""
