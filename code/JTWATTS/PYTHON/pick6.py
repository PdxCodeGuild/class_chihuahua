# I have to run with let say x in range of 1-99 and keep 6 of the numbers
#tickets cost $2
#1 match is $4
#2match is $7
#3 match $100
#4 match is 50000
#5 match is 1,000,000
#6 match is 25,000,000
#tickets only contain 6 numbers
"""
import random

def num_matches():
    other_list = []
    while len(other_list) <=99999:
        ringer = random.randint(1,99)
        other_list.append(ringer)
    # return other_list    
    return len(other_list)
print(num_matches())


def pick6():
    num_list = []
    while len(num_list) <5:
        winner = random.randint(1,99)
        num_list.append(winner)
    return num_list    
print(pick6())

def matching():
    if pick6() in num_matches():
        return map()
while pick6() in num_matches():
    for x in num_matches():
        print()
"""
"""
iterate num matcheing over pick6 for matches.  
understand that they have to be in the percise location in the list to count
where do you place the results


while tally !=99999:
    tally = []
    if pick6[0] == num-list[0]
        tally.append(pick6[0])
    return tally    
        
    if pick6[1] == num-list[1]
        tally.append(pick6[1])
    return tally  
    if pick6[2] == num-list[2]
        tally.append(pick6[2])
    return tally  
    if pick6[3] == num-list[3]
        tally.append(pick6[3])
    return tally  
    if pick6[4] == num-list[4]
        tally.append(pick6[4])
    return tally  
    if pick6[5] == num-list[5]
        tally.append(pick6[5])
    return tally  

"""

"""

#if item in ticket
# import random
# def pick6():
#     pick6_win = []
#     for picks in random.randint(1,99):
#         while len(pick6_win) != 5:
#             pick6_win += picks
#         return pick6_win
# print(pick6())            
           
#             pick6_win += s
#             return pick6_win    
#     print(pick6()) 
# print(pick6())             
#         return random.randint(6)
# print(pick6()) 
# 
"""  
"""
my_ticket = ['a', 'b', 'c', 'd']
random_ticket = ['a', 'c','e' ,'d']

# for x in range(0,4)
counter = 0
for char in range(len(my_ticket)):
  if my_ticket[char] == random_ticket[char]:
    print("we have match", char)
    counter+=1
"""


import random

tally=[]
# combine=0
def num_matches():
    other_list = []
    while len(other_list) <=5:
        ringer = random.randint(1,99)
        other_list.append(ringer)    
    return other_list
print(num_matches())

def pick6():
    num_list = []
    while len(num_list) <=5:
        winner = random.randint(1,99)
        num_list.append(winner)
    return num_list    
print(pick6())

def pic_match():
    tally=[]
    # combine=[]
    winning_ticket = pick6()
    random_ticket = num_matches()
    combine=[]
    while len(combine)<=9:
        combine=[]
        for win in range(len(winning_ticket)):
            while winning_ticket[win]!= random_ticket[win]: 
                add_me = range(1)
                tally.append(add_me)
            break
        combine=[]    
        for win in range(len(winning_ticket)):
            if winning_ticket[win]== random_ticket[win]:
                print("we matched on", win)
                add_me = range(1)
                combine.append(add_me)
            break

        return combine    
        if combine==99999:
                print("100,000 tries have been attempted")  
                       
                return tally
pic_match()
print(pic_match())
# print(combine)
# print(tally)