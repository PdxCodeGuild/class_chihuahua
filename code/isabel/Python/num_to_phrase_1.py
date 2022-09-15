
single_digits = {
    0 : 'zero', 
    1 : 'one', 
    2 : 'two', 
    3 : 'three', 
    4 : 'four', 
    5 : 'five', 
    6 : 'six', 
    7 : 'seven', 
    8 : 'eight', 
    9 : 'nine'
}

double_digits = {
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eightteen',
    19 : 'nineteen'
}

tens_digits = {
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifity',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety'
}

hundreds = {
    100 : 'hundred',
    200 : 'two hundred',
    300 : 'three hundred',
    400 : 'four hundred',
    500 : 'five hundred',
    600 : 'six hundred',
    700 : 'seven hundred',
    800 : 'eight hundred',
    900 : 'nine hundred'
}

# def num_to_phrase(num):
#     translated_number = single_digits[num]
#     return translated_number

# print(num_to_phrase(5))

def num_to_phrase(num):

    if num % 10 < 1 and num % 10 != 0:
        translated_number = single_digits[num]
        return translated_number
    if num // 10 == 1:
        translated_number = double_digits[num]
        return translated_number

print(num_to_phrase(10))

