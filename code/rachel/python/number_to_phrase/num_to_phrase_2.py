ones = {
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
}

# initialized
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

def num_to_phrase(num):
    if num <= 9:
        return ones[num]
    
    elif num >= 10 and num <= 19:
        return teens[num]

    elif num >= 20 and num <= 99:
        tens_digit = int(num // 10)
        ones_digit = int(num % 10)
        #print(ones_digit)
        return (tens[tens_digit] + " " + ones[ones_digit])
    
    elif num > 99:
        hundreds = int(num // 100)
        # print(hundreds)
        new_num = num - (hundreds * 100)
        # print(new_num)
        
        if new_num <= 9:
            return (ones[hundreds] + " hundred " + ones[new_num])

        elif new_num >= 10 and new_num <= 19:
            return (ones[hundreds] + " hundred " + teens[new_num])
            #print(ones[hundreds] + " hundred " + teens[new_num])
        
        elif new_num >= 20 and new_num <= 99:
            tens_digit = int(new_num // 10)
            ones_digit = int(new_num % 10)
            return (ones[hundreds] + " hundred " + tens[tens_digit] + " " + ones[ones_digit])
       
print(num_to_phrase(105))   



     
    