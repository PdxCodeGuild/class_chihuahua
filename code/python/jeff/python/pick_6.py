import random

#dictionary for pricing
matches = {
1: 4,
2: 7,
3: 100,
4: 50000,
5: 1000000,
6: 25000000
}

#player bank
bank = ()
lottery_numbers = []

#Generate 6 random numbers between 1 and 99
def bank_of_numbers():
    for i in range(10):
        random_list = random.sample(range(1, 10), 6)
        print(random_list)
        return lottery_numbers



def user_numbers():
    random_list = random.sample(range(1, 10), 6)
    if user_numbers == random_list:
        random_list = True
        return bank + matches[6]
    elif user_numbers == random_list(5):
        random_list = True  
        return bank + matches[5]


'''
user_list = []


for num in range(0, 6):
    numb = int(input('\nPlease enter a two digit number between 1 and 99: \n'))
    if numb < 9:
        print("Your number is too low: ")

    if numb > 99:
        print("Your number is too high: ")

    else:
        user_list.append(numb) # adding the element

      
print(user_list)

'''

'''def user_numbers():
    user_input = int(input('\nPlease enter a two digit number between 1 and 99: \n'))
    if user_input < 9:
        f"Your number is too low: "
    if user_input > 99:
        f"Your number is too high: "
    else:
        user_list.append(user_numbers)
    
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
random_numbers = []

random_numbers = [random.randint(1, 100) for x in range(6)]

#append list of numbers to list
lottery_list.append(random_numbers)
print(random_numbers)
'''


'''
random_numbers = []

while random_numbers 
    for num in range(0,6):
    numbers = random.randint(1,100)
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