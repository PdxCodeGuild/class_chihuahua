# Jimi Spier
# pick6.py
# 20220919

import random 

def pick6():
    random_numbers_computer =[random.randint(0,10) for nums in range(1,7)]
    random_numbers_user = [random.randint(0,10) for nums in range(1,7)]
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
    winning_streak = 0
    purse = 0
    for num in range(random.randint(150,1200)): #how many times to run game
        user_number, computer_number = pick6() # spits out numbers for both opponents

        winning = num_matches(user_number, computer_number) # see how many numbers match and reveal number matched
        if winning > 0:
            user_profit = money_bag(winning)
            purse = purse + user_profit # adds winning to winning streak
            #print(purse)
        

        
        print(user_number)
        print(computer_number)
     #take value from winning streak and send it to money bag to get winning value
     
    return purse - ticket_cost

print(f"Your winnings (minus ticket cost):${main()}")
