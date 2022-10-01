# Jimi Spier
# pick6.py
# 20220919

import random 

def pick6():
    random_numbers_computer =[random.randint(0,99) for nums in range(1,7)]
    random_numbers_user = [random.randint(0,99) for nums in range(1,7)]
    return random_numbers_user, random_numbers_computer


def num_matches(user_number, computer_number):
    winning = 0
    for num in range(6):
        if user_number[num] == computer_number[num]:
            winning +=1
        else:
            continue
    #print(winning)
    
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
    ticket_cost = 2
    user_profit = [] #empty list to hold user profits
    expense = 0
    purse = 0
    final_total = 0
    for num in range(10000): #how many times to run game
        expense += ticket_cost
        user_number, computer_number = pick6() # spits out numbers for both opponents

        winning = num_matches(user_number, computer_number) # see how many numbers match and reveal number matched
        if winning > 0:
            user_profit = money_bag(winning)
            purse = (purse + user_profit) - ticket_cost # adds winning to winning streak
            print(expense)
        

        
        print(user_number)
        print(computer_number)
        final_total = purse - ticket_cost

     

     
    return final_total

print(f"Your winnings (minus ticket cost):${main()}")
