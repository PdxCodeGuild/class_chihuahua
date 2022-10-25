import random

#again for no confusion to call the function
# random_ticket = num_matches()
# tally=[]
# combine=0
#this funct is to define a random list of 6 to compair to the winning ticket
other_list=[]
def num_matches():
    other_list = []
    while len(other_list) <=5:
        ringer = random.randint(1,99)
        other_list.append(ringer)    
    return other_list
    
# print(num_matches())
# this funct is to gather 6 random numbers as the winning ticket
num_list=[]
def pick6():
    num_list = []
    while len(num_list) <=5:
        winner = random.randint(1,99)
        num_list.append(winner)
    return num_list    
# print(pick6())
#just so there is no confusion
winning_ticket = pick6()
#again for no confusion to call the function
random_ticket = num_matches()
#combine=[]
char=[]
counter=0
def winning_results():
    char=[]
    counter=0 
    # winning_ticket
    # random_ticket
    for char in range(len(winning_ticket)):
        # ringer = random.randint(1,99)
        print('test')
        while winning_ticket[char]==random_ticket[char]:
        #while winning_ticket[char]==random_ticket[char]:
        #while winning_ticket[char]==random_ticket[char]:
            char=[]
            counter=0 
            print(("we have a match",char))
            counter+=1
            char+=char
        print(char,counter,winning_ticket,random_ticket)    
    # print(counter,char)
                     
# how to run for win with  a counter next to each output then only print if they match
# def all_up():
#     for win in range(len(other_list)):
#         combine=[]
#         while len(combine)<5 and other_list[win]== num_list[win] :
#             add_me+=win
#             #add_me = ('1')
#             combine.append(add_me)  
#            # if winning_ticket[win]== random_ticket[win]:
#             print("we matched on", win) 
#         return combine    
# def done_deal():        
#         tried=[]
#         while len(tried)<99999:
#             all_up()

#             tried.append('2')
#         return tried,all_up()
            
#             n(winning_ticket)):
# #             # combine=[]
# #             while winning_ticket[win]!= random_ticket[win]: 
#                 tally2=[]
#                 add_me = 1
#                 tally2.append(add_me)   
            # break
# counter=[]            
# while len(counter) <99999:
#      counter+=1
# counter=0
# while counter<99999:
#     counter=0
#     winning_results()
#     counter+=1    
print(winning_results())
#print(done_deal(),counter)            
# print(winning_ticket) 
# print(random_ticket)           
#print(pick6())
#print(num_matches())
# print(all_up())
# print(4*(TITLES.count(1))+7*(TITLES.count(2))+100*(TITLES.count(3))+50000*(TITLES.count(4))+1000000*(TITLES.count(5))+25000000*(TITLES.count(6))+ -2)