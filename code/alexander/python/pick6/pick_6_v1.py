import random

winning_number = [random.randint(1,10) for num in range(6)]

money_count = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}

def num_matches():
    balance = 0
    ticket_quantity = 0
    grand_total = 0
    while ticket_quantity < 100000:
        ticket_generated = [random.randint(1,100) for num in range(6)]
        balance -= 2
        counter = 0
        for char in range(len(winning_number)):
            if winning_number[char] == ticket_generated[char]:
                counter += 1
        print(counter)
        grand_total += money_count[counter]
        counter = 0 
        ticket_quantity += 1 
        print(balance)
num_matches()