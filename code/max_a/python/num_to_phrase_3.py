# Version 3
from distutils.command.build_scripts import first_line_re
from math import floor

def num_to_phrase(num):
    ones_str = {
        0: "",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX"
    }
    tens_str = {
        0: "",
        1: "X",
        2: "XX",
        3: "XXX",
        4: "XL",
        5: "L",
        6: "LX",
        7: "LXX",
        8: "LXXX",
        9: "XC",
    }
    hundreds_str = {
        0: "",
        1: "C",
        2: "CC",
        3: "CCC",
        4: "CD",
        5: "D",
        6: "DC",
        7: "DCC",
        8: "DCCC",
        9: "CM",    }
    
    ones_digit = num % 10
    tens_digit = int(floor(num // 10))
    if len(str(tens_digit)) == 2:
        tens_digit = str(tens_digit)
        tens_digit = tens_digit[1:] # removes hundreds digit from this variable
        tens_digit = int(tens_digit)
    hundreds_digit = int(floor(num // 100))
    
    word = ""

    substr_one = ones_str[ones_digit]
    substr_ten = tens_str[tens_digit]
    substr_hundred = hundreds_str[hundreds_digit]

    word = f"{substr_hundred}{substr_ten}{substr_one}"

    while word.endswith(" "):
        word = word[:-1]
    while word.startswith(" "):
        word = word[1:]

    return word

print(num_to_phrase(999))
