# Jimi Spier
# file_name.py
# 20220916

# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled

nums_list = [1,2,3,4,5,6]


def double_numbers(nums):
    new_list = []
    for num in nums:
        new_list.append(num * 2) # 
    return new_list #returns new list after construction

def test_double_numbers(): #testing function
    assert double_numbers([1, 2, 3]) == [2, 4, 6]


# Stars
# Write a function that takes an integer and returns that number of asterisks in a string

def stars(n=0): 
       
    return "*" * n # return the value of n multiplied by the string "*"
        
     

def test_stars(): #testing function
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'


# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    new_list = [] #empty list
    for numbers in nums: #seperate the list one number at a time. 
        if numbers < 10: #look for all number that are less than 10
            new_list.append(numbers) #Append numbers that are less than 10 to the new_list
        else:
            continue #if 10 or great, continue without appending to list. 
    return new_list #returns the newly constructed list
    

    

def test_extract_less_than_ten(): #testing function
    assert extract_less_than_ten([2, 8, 12, 18]) == [2, 8]



