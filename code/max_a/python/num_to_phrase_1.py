# Version 1
from math import floor

def num_to_phrase(num):
    special_str = { # these numbers do not follow the same rules as most others
        0: "zero",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        15: "fifteen",
    }
    ones_str = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    tens_str = {
        0: "",
        1: "teen", # make exception; this goes after the ones
        2: "twenty",
        3: "thirty",
        4: "fourty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
        10: "one hundred"
    }
    ones_digit = num % 10
    tens_digit = int(floor(num // 10))
    word = ""
    substr_one = ones_str[ones_digit]
    substr_ten = tens_str[tens_digit]

    if num in list(special_str.keys()):
        word = special_str[num]
    elif tens_digit == 1:
        word = f"{substr_one}{substr_ten}"
    else:
        word = f"{substr_ten} {substr_one}"
    
    if word.endswith(" "):
        word = word[:-1]
    elif word.startswith(" "):
        word = word[1:]

    return word

print(num_to_phrase(100))
