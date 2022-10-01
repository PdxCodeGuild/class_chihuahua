import random

def pick6():
    winning = []
    n = 6
    for i in range(n):
        winning.append(random.randint(1,100))
    print(winning)
    ticket = []
    n = 6
    for i in range(n):
        ticket.append(random.randint(1,100))
    print(ticket)

    def num_matches(winning, ticket):
        while ticket in winning:
            if ticket[0] == winning[0]:
                print("You have 1 match")
            elif ticket[0, 1] == winning[0, 1]:
                print("You have 2 matches")
            elif winning == ticket:
                print("Your ticket matches the winning ticket")
    
        num_matches(winning, ticket)

pick6()
