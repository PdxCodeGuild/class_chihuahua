
# Practice 2: Booleans, Comparisons, & Conditionals
# Copy and paste this file into your own "02_booleans.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 02_booleans.py"


# Go Hiking
# Write a function that takes a string indicating energy level and weather

def go_hiking(energy, weather):

    what_weather = weather
    how_feeling = energy
    
    # feeling_weather_dict = {
    #     'tired' : 'sunny',
    #     'tired' : 'rainy',
    #     'spry' : 'sunny',
    #     'spry' : 'rainy'
    #     }


    if how_feeling == 'spry' and what_weather == 'sunny':
        return True     
    elif how_feeling == 'tired' or what_weather == 'rainy':
        return False
    else:
        return 'invalid'

print("Instructions: please choose one feeling: 'tired' or 'spry' and one weather type: 'rainy' or 'sunny'")
how_feeling = input('How are you feeling today? ')
what_weather = input("What's the weather? ")
print(go_hiking(how_feeling, what_weather))

# def test_go_hiking():
#     assert go_hiking('tired', 'rainy') == False
#     assert go_hiking('tired', 'sunny') == False
#     assert go_hiking('spry', 'rainy') == False
#     assert go_hiking('spry', 'sunny') == True


# # Double Digit
# # Write a function that returns True if the number is a double digit

# def double_digit(num):
#     ...

# def test_double_digit():
#     assert double_digit(5) == False
#     assert double_digit(55) == True
#     assert double_digit(672) == False
#     assert double_digit(-56) == True


# # Opposite
# # Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.

# def opposite(a, b):
#     ...

# def test_opposite():
#     assert opposite(10, -1) == True
#     assert opposite(2, 3) == False
#     assert opposite(-1, -1) == False


# # Near 100
# # Write a function that returns True if a number within 10 of 100.


# def near_100(num):
#     ...

# def test_near_100():
#     assert near_100(50) == False
#     assert near_100(99) == True
#     assert near_100(105) == True
#     assert near_100(115) == False


# # Maximum of Three
# # Write a function that returns the maximum of 3 parameters.


# def maximum_of_three(a, b, c):
#     ...

# def test_maximum_of_three():
#     assert maximum_of_three(5,6,2) == 6
#     assert maximum_of_three(-4,3,10) == 10
