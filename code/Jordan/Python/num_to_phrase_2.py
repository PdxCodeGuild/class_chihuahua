single_digit_words = {
0: "", 1: "one", 2: "two",  3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
8: "eight", 9: "nine", }
teen_words = {10: "ten",  11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
17: "seventeen", 18: "eighteen", 19: "nineteen"}
double_digit_words = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
hundreds = {100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred", 500: "five hundred",
600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred"
            }

def num_to_phrase(num):
    ones_digit = num%10
    tens_digit = (num//10) % 10 * 10
    if 9 < (ones_digit + tens_digit) < 20:
        teens_digit = tens_digit + ones_digit
    else:
        teens_digit = False
    hundreds_digit = (num//100) * 100

    if num < 10:
        return single_digit_words[ones_digit]
    elif num < 20:
        return teen_words[teens_digit]
    elif num < 100:
        if ones_digit == 0:
            return double_digit_words[tens_digit]
        return (f"{double_digit_words[tens_digit]} {single_digit_words[ones_digit]}")
    else:
        if tens_digit == 0 and ones_digit == 0:
            return hundreds[hundreds_digit]
        elif tens_digit == 0 and teens_digit == False: # create a condition to find values between 100s to 109
            return (f"{hundreds[hundreds_digit]} {single_digit_words[ones_digit]}")
        elif teens_digit != False:
            return (f"{hundreds[hundreds_digit]} {teen_words[teens_digit]}")
        else:
            txt = (f"{hundreds[hundreds_digit]} {double_digit_words[tens_digit]} {single_digit_words[ones_digit]}")
            no_space = txt.strip()
            return no_space

print(num_to_phrase(999))

def test_num_to_phrase_2():
    assert num_to_phrase(1) == "one"
    assert num_to_phrase(5) == "five"
    assert num_to_phrase(10) == "ten"
    assert num_to_phrase(11) == "eleven"
    assert num_to_phrase(15) == "fifteen"
    assert num_to_phrase(19) == "nineteen"
    assert num_to_phrase(55) == "fifty five"
    assert num_to_phrase(70) == "seventy"
    assert num_to_phrase(82) == "eighty two"
    assert num_to_phrase(99) == "ninety nine"
    assert num_to_phrase(100) == "one hundred"
    assert num_to_phrase(101) == "one hundred one"
    assert num_to_phrase(212) == "two hundred twelve"
    assert num_to_phrase(650) == "six hundred fifty"
    assert num_to_phrase(999) == "nine hundred ninety nine"