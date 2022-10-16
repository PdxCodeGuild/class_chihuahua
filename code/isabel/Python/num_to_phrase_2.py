# def num_to_phrase(num):
#     pass
   
# print(num_to_phrase(591))
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
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety'
}

hundreds = {
    100 : 'one hundred',
    200 : 'two hundred',
    300 : 'three hundred',
    400 : 'four hundred',
    500 : 'five hundred',
    600 : 'six hundred',
    700 : 'seven hundred',
    800 : 'eight hundred',
    900 : 'nine hundred'
}


def num_to_phrase(num):
    tens_or_floor = num // 10 >= 2 and num // 10 < 10
    
    hundreds_or_floor = num // 100 >= 1
    if num // 10 == 0 and num % 10 >= 0:
        translated_number = single_digits[num]
        return translated_number
    if num // 10 == 1:
        translated_number = double_digits[num]
        return translated_number
    if tens_or_floor and num % 10 == 0:
        translated_number = tens_digits[num]
        return translated_number
    if num - (num % 10) in tens_digits:
    
        translated_number = f"{tens_digits[num - (num % 10)]} {single_digits[num % 10]}"  
        return translated_number
    if hundreds_or_floor and num % 100 == 0:
        translated_number = hundreds[num]
        return translated_number
    if hundreds_or_floor and num % 100 != 0:
        next_digit = num % 100
        first_hundreds_digit = num - (num % 100)
        if next_digit in single_digits:
            translated_number = f"{hundreds[first_hundreds_digit]} {single_digits[next_digit]}"
            return translated_number
        elif next_digit in double_digits:
            translated_number = f"{hundreds[first_hundreds_digit]} {double_digits[next_digit]}"
            return translated_number
        elif next_digit in tens_digits:
            translated_number = f"{hundreds[first_hundreds_digit]} {tens_digits[next_digit]}"
            return translated_number
        elif next_digit % 10 != 0:
            last_digit = next_digit % 10
            whole_next_digit = next_digit - (last_digit)
            translated_number = f"{hundreds[first_hundreds_digit]} {tens_digits[whole_next_digit]} {single_digits[last_digit]}"
            return translated_number
    

print(num_to_phrase(100))
