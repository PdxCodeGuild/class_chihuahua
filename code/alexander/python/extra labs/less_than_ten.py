# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.
nums = [2, 8, 12, 18]
less_than_ten = []


def extract_less_than_ten(nums):
    for num in nums:
        if num < 10:
            less_than_ten.append(num)
extract_less_than_ten(nums)
print(less_than_ten)

def test_extract_less_than_ten():
    assert extract_less_than_ten([2, 8, 12, 18]) == [2, 8]
