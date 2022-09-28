import random

#Generate 6 random numbers between 1 and 99
for i in range(1000):
    random_list = random.sample(range(1, 100), 6)
    print(random_list)
      
#print(user_list)

#user_input = []
'''def user_numbers():
    user_input = int(input('\nPlease enter a two digit number between 1 and 99: \n'))
    if user_input < 9:
        f"Your number is too low: "
    if user_input > 99:
        f"Your number is too high: "
    else:
        user_list.append(user_numbers,6)
    
print(user_list)
'''
'''

# creating an empty list
lst = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
print(lst)

'''
'''
lottery_list = []

random_numbers = [random.randint(1, 100) for x in range(6)]

#append list of numbers to list
lottery_list.append(random_numbers)
print(random_numbers)

'''
'''

random_numbers = []

while random_numbers: 
    for num in range(0,6):
    number = random.randint(1,100)
    random_numbers.append(numbers)
    print(random_numbers)

'''
'''
a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
'''