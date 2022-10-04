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
    10 : 'ten',
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

hundreds = {
    100 : 'one hundred',
    200 : 'two hundred',
    300 : 'three hundred',
    400 : 'four hundred',
    500 : 'five hundred',
    600 : 'six hundred',
    700 : 'seven hundred',
    800 : 'eight hundred',
    900 : 'nine hundred',
    1000 : 'one thousand'
}

hundreds_digit = {
    1 : 'one hundred',
    2 : 'two hundred',
    3 : 'three hundred',
    4 : 'four hundred',
    5 : 'five hundred',
    6 : 'six hundred',
    7 : 'seven hundred',
    8 : 'eight hundred',
    9 : 'nine hundred',
    10 : 'one thousand'
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
            second_digit = num//10
            third_digit = num%10
            return f"{tens_digit[second_digit]} {ones_digit[third_digit]}"
    if num in range(100,1000): #100's 50's and teens
        first_digit = num//100  
        second_digit = num%100 
        third_digit = second_digit%10 
        if num % 100 == 0:
            return hundreds[num]
        elif second_digit in divisible_ten_digits:
            return f"{hundreds_digit[first_digit]} {divisible_ten_digits[second_digit]}"
        elif second_digit in teen_digits:
            return f"{hundreds_digit[first_digit]} {teen_digits[second_digit]}"
    if num in range(100,1000):
        first_digit_1 = num//100
        first_digit_mult = first_digit_1 * 10
        second_digit_2 = num//10 - first_digit_mult
        third_digit_3 = num%10
        if first_digit_1 in hundreds_digit and second_digit_2 in tens_digit and third_digit_3 in ones_digit:
            return f"{hundreds_digit[first_digit_1]} {tens_digit[second_digit_2]} {ones_digit[third_digit_3]}"
        else:
            return f"{hundreds_digit[first_digit_1]} {ones_digit[third_digit_3]}"



print(num_to_phrase(965))

        
    
