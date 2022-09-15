
def num_to_phrase(num):
    numbers = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred"
    }
    if num == 0:
        return "zero"
    elif num <= 20:
            return numbers[num]
    elif num <= 100:
        return numbers[(num//10)*10] + " " + numbers[(num%10)]
    

print(num_to_phrase(97))
'''
x = 67
tens_digit = x//10
ones_digit = x%10

'''