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
won=0
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
    won+=money[counter]        
    total+=money[counter] 
    total-=2
    counter=0
ROI=total-won    
print("Your ROI is",ROI)