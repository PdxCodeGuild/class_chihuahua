import random

#user numbers
def user_nums():
    numbers = []
    for num in range(6):
        numbers.append(random.randint(1, 99))
    return numbers

#computer generated numbers
def winning_nums(first, second):
    matches = 0
    for index in range(len(first)):
        if first[index] == second[index]:
            matches += 1
    return matches

#define win parameters
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

#starting balances
bank = 0
loss = 0
win = 0

#amount of times played
loop = 10

for l in range(loop):
    bank -= 2
    loss += 2
    result = start_game(winning)
    bank += result
    win += result


#print bank, winnings and ammt spent
print(f"Bank: ${bank}")
print(f"Won: ${win}")
print(f"Spent: ${loss}")
#ROI statement
print(f"ROI: ${(win - loss)/loss}")