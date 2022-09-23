import random

def random_numbers(times):
    six_numbers = []
    for i in range(times):
        number = random.randint(1, 99)
        six_numbers.append(number)
    return six_numbers

def compare_sets(x, y):
    a = set(x)
    b = set(y)
    return a & b



# winning_ticket = random_numbers(6)
# my_ticket = random_numbers(6)

''' test variables and statements   
winning_ticket = [3, 45, 22, 86, 34, 5]
my_ticket = [3, 65, 23, 47, 5, 34]
a = set(winning_ticket)
b = set(my_ticket)
print(compare_sets(winning_ticket, my_ticket))
print(matching_tickets(winning_ticket, my_ticket))
'''

balance = 0

def pick6():
    balance = 0
    winning_numbers = random_numbers(6)
    for i in range(1000):
        ticket = random_numbers(6)
        balance -= 2
        print(balance)
        same_numbers = []
        same_numbers.append(compare_sets(winning_numbers, ticket))
        print(same_numbers)
        for num in same_numbers:
            balance += 5
            print(balance)
    
pick6()