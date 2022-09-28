import random

def random_numbers(times):
    six_numbers = []
    for i in range(times):
        number = random.randint(1, 99)
        six_numbers.append(number)
    return six_numbers
6
def pick6():
    balance = 0
    winning_numbers = random_numbers(6)
    for i in range(100000):
        ticket = random_numbers(6)
        balance -= 2
        print(balance)
        same_numbers = []
        for num in ticket:
            if num in winning_numbers:
                same_numbers.append(num)
            while len(same_numbers) > 0:
                if len(same_numbers) == 0:
                    balance += 0
                    return balance
                elif len(same_numbers) == 1:
                    balance += 2
                    return balance
                elif len(same_numbers) == 2:
                    balance += 7
                    return balance
                elif len(same_numbers) == 3:
                    balance += 100
                    return balance
                elif len(same_numbers) == 4:
                    balance += 50000
                    return balance
                elif len(same_numbers) == 5:
                    balance += 1000000
                    return balance
                elif len(same_numbers) == 6:
                    balance += 25000000
                    return balance

print(pick6())

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

# balance = 0
# def compare_sets(x, y):
#     a = set(x)
#     b = set(y)
#     return a & b
# def pick6():
#     balance = 0
#     winning_numbers = random_numbers(6)
#     for i in range(1000):
#         ticket = random_numbers(6)
#         balance -= 2
#         print(balance)
#         same_numbers = []
#         same_numbers.append(compare_sets(winning_numbers, ticket))
#         print(same_numbers)
#             while len(same_numbers) > 0:
                            
# pick6()