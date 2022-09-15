# def num_to_phrase(num):
#     pass


# print(num_to_phrase(5))
singles = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
tens = {10:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
doubles = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}

def num_to_phrase():
    x = int(input("Please enter a number: "))
    tens_digit = (x//10)
    ones_digit = (x%10)

num_to_phrase()
    # if tens_digit == 1 and ones_digit == 0:
    #     print("ten")
    # elif tens_digit == 1 and ones_digit == 1:
    #     print("eleven")
    # elif tens_digit == 1 and ones_digit == 2:
    #     print("twelve")
    # elif tens_digit == 1 and ones_digit == 3:
    #     print("thirteen")
    # elif tens_digit == 1 and ones_digit == 4:
    #     print("fourteen")
    # elif tens_digit == 1 and ones_digit == 5:
    #     print("fifteen")
    # elif tens_digit == 1 and ones_digit == 6:
    #     print("sixteen")
    # elif tens_digit == 1 and ones_digit == 7:
    #     print("seventeen")
    # elif tens_digit == 1 and ones_digit == 8:
    #     print("eighteen")
    # elif tens_digit == 1 and ones_digit == 9:
    #     print("nineteen")
    # elif tens_digit == 2:
    #     print("twenty")
    # elif tens_digit == 3:
    #     print("thirty")
    # elif tens_digit == 4:
    #     print("forty")
    # elif tens_digit == 5:
    #     print("fifty")
    # elif tens_digit == 6:
    #     print("sixty")
    # elif tens_digit == 7:
    #     print("seventy")
    # elif tens_digit == 8:
    #     print("eighty")
    # elif tens_digit == 9:
    #     print("ninety")
    # elif ones_digit == 1:
    #     print("one")
    # elif ones_digit == 2:
    #     print("two")
    # elif ones_digit == 3:
    #     print("three")
    # elif ones_digit == 4:
    #     print("four")
    # elif ones_digit == 5:
    #     print("five")
    # elif ones_digit == 6:
    #     print("six")
    # elif ones_digit == 7:
    #     print("seven")
    # elif ones_digit == 8:
    #     print("eight")
    # elif ones_digit == 9:
        
# print(tens_digit)
# print(ones_digit)