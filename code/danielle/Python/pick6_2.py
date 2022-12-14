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
    winning_ticket = pick6()
    for n in range(5):
        return ticket
    for n in range(1):
        return winning_ticket
    print(f"{ticket} and {winning_ticket}")

lottery()

