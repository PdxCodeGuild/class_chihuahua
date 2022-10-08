import random
money={
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5: 1000000,
    6: 25000000
}
def pick_6():
    other_list = []
    for other in range(0,6):
        other_list.append(random.randint(1,99))    
    return other_list


winning_ticket = pick_6()
total=0

char_list=[]
for x in range(0,99999):
    counter=0
    random_ticket = pick_6()
    print('winning ticket', winning_ticket)
    print('random ticket', random_ticket)
    
    for char in range(len(winning_ticket)):
        # char=[]
        if winning_ticket[char] == random_ticket[char]:
            
            print("We have a match", char)
            counter+=1
            
            print(counter)
            
    total+=money[counter] 
    total-=2
    counter=0
print("this is how much you made or loss",total)

# def ticket():
#   nums = []

#   for num in range(0,7):
#     nums.append(random.randint(0,5))
#   return nums


# my_ticket = ticket()

# for x in range(0,9):
#   random_ticket = ticket()
#   print('my ticket', my_ticket)
#   print('random ticket', random_ticket)

#   def num_matches():
#     other_list = []
#     for other_list in range(0,5):
#         other_list.append(random.randint(1,99))
           
#     return other_list

# # this funct is to gather 6 random numbers as the winning ticket
# num_list=[]
# def pick6():
#     num_list = []
#     while len(num_list) <=5:
#         winner = random.randint(1,99)
#         num_list.append(winner)
#     return num_list    
 



