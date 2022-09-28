'''x = (10)
tens_digit = x//10
ones_digit = x%10
'''


tens_digit = {
    2 : 'twenty',
    3 : 'thirty',
    4 : 'forty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety',
    10 : 'ten'
}

divisible_ten_digits = {
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety'
}

teen_digits = {
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
}


ones_digit = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten'
}

def num_to_phrase(num):
    if num in range(0,11):
        return ones_digit[num]
    if num in range(11,20):
        return teen_digits[num]
    if num in range(20,100):
        if num % 10 == 0:
            return divisible_ten_digits[num]
        else:
            first_digit = num//10
            second_digit = num%10
            return f"{tens_digit[first_digit]} {ones_digit[second_digit]}"




print(num_to_phrase(85))