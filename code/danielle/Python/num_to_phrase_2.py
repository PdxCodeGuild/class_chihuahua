def num_to_phrase(num):
    ones_digit = {
        1: "one", 2: "two", 
        3: "three", 4: "four", 
        5: "five", 6: "six", 
        7: "seven", 8:"eight", 
        9: "nine", 10: "ten"
        }
    tens_digit = {
        2: "twenty", 3: "thirty", 
        4: "forty", 5: "fifty", 
        6: "sixty", 7: "seventy", 
        8: "eighty", 9: "ninety"
        }
    teens_digit = {
        11: "eleven", 12: "twelve", 
        13: "thirteen", 14: "fourteen", 
        15: "fifteen", 16: "sixteen", 
        17: "seventeen", 18: "eighteen", 
        19: "nineteen"
        }
    hundreds_digit = {
        100: "one hundred", 200: "two hundred", 
        300: "three hundred", 400: "four hundred", 
        500: "five hundred", 600: "six", 
        700: "seven hundred", 800: "eight hundred", 
        900: "nine hundred" }
    
    if num in range(0, 11):
        return ones_digit[num]
    elif num in range(11, 20):
        return teens_digit[num]
    elif num in range(20, 100):
        return (f"{tens_digit[(num//10)]} {ones_digit[(num%10)]}")
    elif num in range(100, 1000):
        return (f"{hundreds_digit[(num//100)]} {tens_digit[(num//10)]} {ones_digit[(num%10)]}")
        #return tens_digit[num] and ones_digit[num]
        # tens_digit = x//10
        # ones_digit = x%10

num = (input("Please enter a number: "))
print(num_to_phrase((num)))