import random

def random_numbers(times):
    six_numbers = []
    for i in range(times):
        number = random.randint(1, 99)
        six_numbers.append(number)
    return six_numbers

# winning_ticket = random_numbers(6)
# my_ticket = random_numbers(6)

def matching_tickets(winning_ticket, my_ticket):
    winning_numbers = []
    for num in range(0, 6):
        if winning_ticket[num] == my_ticket[num]:
            winning_numbers.append(num)
        return winning_numbers

winning_ticket = [3, 45, 22, 86, 34, 5]
my_ticket = [3, 65, 23, 47, 34, 5]

print(matching_tickets(winning_ticket, my_ticket))