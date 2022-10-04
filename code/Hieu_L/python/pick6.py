import random

def random_numbers(times):
    six_numbers = []
    for i in range(times):
        number = random.randint(1, 99)
        six_numbers.append(number)
    return six_numbers

def compare_sets(winning_numbers, ticket):
    same_number = []
    for num in range(6):
        if ticket[num] == winning_numbers[num]:
            same_number.append(num)
        return same_number

def roi(expenses, earnings):
    roi = (earnings - expenses) / expenses
    return roi

def pick6():
    balance = 0
    earnings = 0
    expenses = 0
    winning_numbers = random_numbers(6)
    for i in range(10000):
        ticket = random_numbers(6)
        balance -= 2
        expenses -= 2
        same_numbers = compare_sets(winning_numbers, ticket)
        while len(same_numbers) > 0:
            if len(same_numbers) == 1:
                balance += 2
                earnings += 2
            elif len(same_numbers) == 2:
                balance += 7
                earnings += 7
            elif len(same_numbers) == 3:
                balance += 100
                earnings += 100
            elif len(same_numbers) == 4:
                balance += 50000
                earnings += 50000
            elif len(same_numbers) == 5:
                balance += 1000000
                earnings += 1000000
            elif len(same_numbers) == 6:
                balance += 25000000
                earnings += 25000000
            else:
                balance += 0
                earnings += 0
    print(roi(expenses, earnings))
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