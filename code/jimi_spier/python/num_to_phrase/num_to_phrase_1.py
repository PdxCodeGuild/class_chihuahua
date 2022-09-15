



def num_to_phrase(num):

    number_dict = {
        0 : "",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
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
        30: "thrity",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "one hundred"
    }
    tens_digit = num // 10
    ten_digit_isolated = tens_digit * 10
    ones_digit = num % 10

    tens_word = ""
    ones_word = ""
    if ten_digit_isolated >= 10:
        tens_word = number_dict[ten_digit_isolated]
        ones_word = number_dict[ones_digit]
    else:
        tens_word = ""
        ones_word = number_dict[ones_digit]
    return (f"Your number is: {tens_word} {ones_word}")

       


print(num_to_phrase(21))
 