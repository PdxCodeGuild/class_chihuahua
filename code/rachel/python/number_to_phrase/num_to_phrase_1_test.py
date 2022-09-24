ones = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

teens = {
    10: "ten",
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
} 

#num = input("enter a number: ")
#num = int(num)

def num_to_phrase(num):
    if num <= 9:
        return ones[num]
    
    elif num >= 10 and num <= 19:
        return teens[num]

    elif num >= 20 and num <= 99:
        tens_digit = int(num // 10)
        ones_digit = int(num % 10)
        return (tens[tens_digit] + " " + ones[ones_digit])
    
    elif num > 99:
        return ("number out of range") 

print(num_to_phrase(15))   



     
    