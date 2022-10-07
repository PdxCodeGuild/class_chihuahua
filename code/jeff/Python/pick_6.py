import random

#class Pick6:

def user_nums():
    numbers = []
    for num in range(6):
        numbers.append(random.randint(1, 99))
    return numbers

def winning_nums(first, second):
    match = 0
    for index in range(len(first)):
        if first[index] == second[index]:
            match += 1
    return match

def start_game(winners):
    winning_key = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 100000,
        6: 25000000
    }
    ticket = user_nums()
    score = winning_nums(winners, ticket)
    return winning_key[score]

winning = user_nums()
#starting balances. Bank starts with $100 
bank = 100
loss = 0
win = 0


#loops to play set ammount of instances. set ammount with loop
loop = 100000
for l in range(loop):
    bank -= 2
    loss += 2
    result = start_game(winning)
    bank += result
    win += result
    #break loop if user runs out of money
    if bank < 0:
        print(f"you are out of money")
        break


#print statements
print(f"Bank: ${bank}")
print(f"Won: ${win}")
print(f"Spent: ${loss}")


#version 2
print(f"ROI per attempt: ${(win - loss)/loss}")