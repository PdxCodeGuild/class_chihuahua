# Jimi Spier
# pick6_v2.py
# 20220921

import random


def pick6():
    random_numbers_computer = [random.randint(0, 99) for nums in range(1, 7)]
    random_numbers_user = [random.randint(0, 99) for nums in range(1, 7)]
    return random_numbers_user, random_numbers_computer


def num_matches(user_number, computer_number):
    winning = 0
    for num in range(6):
        if user_number[num] == computer_number[num]:
            winning += 1
        else:
            continue
    # print(winning)

    return winning


def money_bag(winning):
    user_wins = {
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
    user_profit = []  # empty list to hold user profits
    expense = 0
    purse = 0
    final_total = 0
    roi = 0
    for num in range(10000):  # how many times to run game
        expense += ticket_cost
        user_number, computer_number = pick6()  # spits out numbers for both opponents

        # see how many numbers match and reveal number matched
        winning = num_matches(user_number, computer_number)
        if winning > 0:
            user_profit = money_bag(winning)
            # adds winning to winning streak
            purse = (purse + user_profit) - ticket_cost
            # print(expense)

        print(user_number)
        print(computer_number)
        final_total = purse - ticket_cost
        roi = (purse - expense)/expense

    return final_total, roi, expense


final_total, roi, expense = main()
float_roi = "{:.2e}".format(roi)
print(
    f"Your winnings (minus ticket cost):${final_total} and your return on investment is: ${float_roi} because you spent: ${expense} on the tickets")
