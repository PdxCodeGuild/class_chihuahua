import random

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
#winning_ticket = pick6()
#again for no confusion to call the function
#random_ticket = num_matches()
#combine=[]

# how to run for win with  a counter next to each output then only print if they match
def all_up():
    for win in range(len(other_list)):
        combine=[]
        while len(combine)<5 and other_list[win]== num_list[win] :
            add_me+=win
            #add_me = ('1')
            combine.append(add_me)  
           # if winning_ticket[win]== random_ticket[win]:
            print("we matched on", win) 
        return combine    
def done_deal():        
        tried=[]
        while len(tried)<99999:
            all_up()

            tried.append('2')
        return tried,all_up()
            
#             n(winning_ticket)):
# #             # combine=[]
# #             while winning_ticket[win]!= random_ticket[win]: 
#                 tally2=[]
#                 add_me = 1
#                 tally2.append(add_me)   
            # break
print(done_deal())            
#print(winning_ticket)            
#print(pick6())
#print(num_matches())
print(all_up())



# range(5)()





















































# def pic_match():
#     tally=[]
#     # combine=[]
#     winning_ticket = pick6()
#     random_ticket = num_matches()
#     combine=[]
#     while len(combine)<=9:
#         combine=[]
#         for win in range(len(winning_ticket)):
#             while winning_ticket[win]!= random_ticket[win]: 
#                 add_me = range(1)
#                 tally.append(add_me)
#             break
#         combine=[]    
#         for win in range(len(winning_ticket)):
#             if winning_ticket[win]== random_ticket[win]:
#                 print("we matched on", win)
#                 add_me = range(1)
#                 combine.append(add_me)
#             break

#         return combine    
#         if combine==99999:
#                 print("100,000 tries have been attempted")  
                       
#                 return tally
# # pic_match()
# print(pic_match())
# # print(combine)
# # print(tally)