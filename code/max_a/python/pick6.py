import random

def generate_set():
    numbers = []
    for num in range(6):
        numbers.append(random.randint(1, 99))
    return numbers

def match_sets(first, second):
    matching = 0
    for index in range(len(first)):
        if first[index] == second[index]:
            matching += 1
    return matching

def play(winners):
    prizes = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 100000,
        6: 25000000
    }
    ticket = generate_set()
    score = match_sets(winners, ticket)
    return prizes[score]

winning = generate_set()

balance = 0
losses = 0
gains = 0

loops = 100000

for loop in range(loops):
    balance -= 2
    losses += 2
    results = play(winning)
    balance += results
    gains += results

print(f"Earnings: ${gains}")
print(f"Expenses: ${losses}")
print(f"Final Balance: ${balance}")
print(f"Return on Investment: ${(gains - losses)/losses} per ticket")