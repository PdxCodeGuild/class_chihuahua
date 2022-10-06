import random 

bank = int(input('\nHow much do you want to deposit?: \n'))
ticket_cost = 2
winning_key= {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    } 

def random_nums():
    winning_instances = ()
    player_numbers = [random.randint(0,100) for num in range(1,7)]
    computer_numbers = [random.randint(0,100) for num in range(1,7)]
    for num in range(10): #how many times to run, change to 10,000
        if player_numbers(0) == computer_numbers(0):
            return winning_instances += 1
        elif player_numbers(1) == computer_numbers(1):
            return winning_instances += 1
        elif player_numbers(2) == computer_numbers(2):
            return winning_instances += 1
        elif player_numbers(3) == computer_numbers(3):
            return winning_instances += 1
        elif player_numbers(4) == computer_numbers(4):
            return winning_instances += 1
        elif player_numbers(5) == computer_numbers(5):
            return winning_instances += 1
        elif player_numbers(6) == computer_numbers(6):
            return winning_instances += 1
        else: return f"No matches"

        



    return player_numbers, computer_numbers,

print(random_nums())



