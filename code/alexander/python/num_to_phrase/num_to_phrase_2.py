
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
    90: "ninety"
    }
    if num == 0:
        return "zero"
    elif num <= 20:
        return numbers[num]
    elif num <= 100:
        return numbers[num//10*10] + " " + numbers[num%10]
    elif num < 1000:
        if num%100 == 0:
            return numbers[num//100] + " hundred"
        elif num%100 < 20:
            return numbers[num//100] + " " + "hundred" + " " + numbers[num%100]
        else:
            first_digit = numbers[num//100]
            second_digit = numbers[(num%100//10)*10]
            third_digit = numbers[num%10]
            return first_digit + " " + "hundred" + " " + second_digit + " " + third_digit

print(num_to_phrase(591))