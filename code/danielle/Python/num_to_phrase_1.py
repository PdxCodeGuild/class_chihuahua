# def num_to_phrase(num):
#     pass


# print(num_to_phrase(5))



def num_to_phrase(num):
    ones_digit = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8:"eight", 9: "nine", 10: "ten"}
    tens_digit = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
    teens_digit = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
    
    if num in range(0, 11):
        return ones_digit[num]
    elif num in range(11, 19):
        return teens_digit[num]
    elif num in range(20, 99):
        return tens_digit(int[num/10]) and ones_digit[num%10]
        #return tens_digit[num] and ones_digit[num]

    #ones_digit == int((num)%10):
    #tens_digit == num_to_phrase(int(num/10)) + ones_digit:
    #     print(tens_digit + ones_digit)

num = (input("Please enter a number: "))
print(num_to_phrase(int(num)))