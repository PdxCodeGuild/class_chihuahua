import random

    
def pick6(list):
    while len(list) < 6:
        list.append(random.randint(1,100))

def computer_attemps(list):
    print(f' Here are the winning numbers: {list}')
    tries = 100000
    money = 0
    condition = 0
    comput_list = []
    six_counter = 0
    five_counter = 0
    four_counter = 0
    three_counter = 0
    two_counter = 0
    one_counter = 0
    
    while tries > -1 or comput_list == list:
        cost = -2
        money += cost
        for x in range(6):
            x = random.randint(1,100)
            comput_list.append(x)
        for x in range(len(list)):
            if comput_list[x] == list[x]:
                condition += 1
                continue

        if condition == 6:
            money += 25000000
            
            condition = 0
            six_counter += 1
        elif condition == 5:
            money += 1000000
            condition = 0
            five_counter += 1
            
        elif condition == 4:
            money += 50000
            condition = 0
            four_counter += 1
            
        elif condition == 3:
            money += 100
            condition = 0
            three_counter += 1
            
        elif condition == 2:
            money += 7
            condition = 0
            two_counter += 1
            
        elif condition == 1:
            money += 4
            condition = 0
            one_counter += 1
            

        if tries == 0:
            print(f"The computer did not guess correctly: {comput_list}")
            print(f'The winning numbers arr as follows:   {list}')
            print(f"YOu have a total of {money} dollars")
            print(f"Matching 6 in a row: {six_counter}")
            print(f"Matching 5 in a row: {five_counter}")            
            print(f"Matching 4 in a row: {four_counter}")
            print(f"Matching 3 in a row: {three_counter}")
            print(f"Matching 2 in a row: {two_counter}")
            print(f"Matching 1 in a row: {one_counter}")
            ROI = money - (tries*cost)
            print(f"The computer's Return on Invstment is: {ROI}")
            break
        elif comput_list == list:
            print("The computer gueesed the correct numbers ")
            print(f'The winning numbers arr as follows:   {list}')
            print(f"Matching 6 in a row: {six_counter}")
            print(f"Matching 5 in a row: {five_counter}")            
            print(f"Matching 4 in a row: {four_counter}")
            print(f"Matching 3 in a row: {three_counter}")
            print(f"Matching 2 in a row: {two_counter}")
            print(f"Matching 1 in a row: {one_counter}")
            ROI = money - (tries*cost)
            print(f"The computer's Return on Invstment is: {ROI}")
            break
        elif comput_list != list:
            print(f'You have {tries} tries remaining')
            comput_list.clear()
            tries -= 1
            continue
        

def main():
    num_list = []

    pick6(num_list)

    

    computer_attemps(num_list)
    
main()