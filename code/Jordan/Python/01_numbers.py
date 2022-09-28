# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    if a % 2 == 0:
        print("It is even")
    else:
        print("It is odd")


def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True
