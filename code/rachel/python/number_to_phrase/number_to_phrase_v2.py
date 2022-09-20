# Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. # # # Handle numbers from 100-999.

# 

hundreds = {
    1: "one hundred",
    2: "two hundred",
    3: "three hundred",
    4: "four hundred",
    5: "five hundred",
    6: "six hundred",
    7: "seven hundred",
    8: "eight hundred",
    9: "nine hundred",
}

teens = {
    0: "ten",
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen",
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

num = input("enter a three digit number: ")
num = list(num)
for i in range(0, len(num)):
    num[i] = int(num[i])

def num_to_phrase(num):

    if num[1] == 0:
        return (hundreds[num[0]] + " " + ones[num[2]])

    elif num[1] == 1:
        return (hundreds[num[0]] + " " + teens[num[2]])

    elif num[1] >= 2:
        tens_digit = (num[1] % 10)
        ones_digit = (num[2] % 10)
        return (hundreds[num[0]] + " " + tens[tens_digit] + " " + ones[ones_digit])

print(num_to_phrase(num))  



     
    
     
    