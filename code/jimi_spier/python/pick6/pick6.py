# Jimi Spier
# pick6.py
# 20220919

import random 

def pick6():
    random_numbers_computer = [random.randint(0,99) for nums in range(1,7)]
    random_numbers_user = [random.randint(0,99) for nums in range(1,7)]
    return random_numbers_user, random_numbers_computer


def num_matches(user_number, computer_number):
    winning = 0
    for num in range(6):
        if user_number[num] == computer_number[num]:
            winning +=1
        else:
            continue
    print(winning)
    
    return winning


def money_bag (winning):
    user_wins= {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000

    }    
    return user_wins[winning]







def main():
    
    user_profit = [] #empty list to hold user profits
    for num in range(10000): #how many times to run game
        user_number, computer_number = pick6() # spits out numbers for both opponents

        winning = num_matches(user_number, computer_number) # see how many numbers match and reveal number matched
        winning_streak =+ winning # adds winning to winning streak
        print(winning_streak)
        

        
        print(user_number)
        print(computer_number)
    user_profit = money_bag(winning_streak) #take value from winning streak and send it to money bag to get winning value
    return print(f"You have won: $ {user_profit}")

print(main())
