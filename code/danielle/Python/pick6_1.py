import random

def pick6():
    winning = []
    user_ticket = []
    n = 6
    for num in range(n):
        winning.append(random.randint(1,100))
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
