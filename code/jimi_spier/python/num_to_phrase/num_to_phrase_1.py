# Jimi Spier
# num_to_phrase_1.py
# 20220914


# ----------------------Function---------------------------------------- #
def num_to_phrase(num):
    # ----------------------Dictionary---------------------------------- #
    number_dict = {
        0 : "",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
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
        30: "thrity",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "one hundred"
    } #dictionary of available keys and values

    # ----------------------Math-------------------------------------------- #
    tens_digit = num // 10 #floor division to isolate tens position as single int
    ten_digit_isolated = tens_digit * 10 # after getting tens position number, multiply by ten to reconstitute
    ones_digit = num % 10 # modulus removes tens and reveals ones value

    tens_word = "" #initialize varible 
    ones_word = "" #initialize varible 
    # ----------------------Processing-------------------------------------- #
    if num > 0 and num < 20:#if the number is between 1 and 19 return value to console
        return number_dict[num] #load value of number_dict[num] and returns to console

    if num == 100: #if the number is 100
        return number_dict[num] #load value of number_dict[num] and returns to console

    if ten_digit_isolated >= 10 and ones_digit > 0: #if the number is above ten and the ones digit is above zero, process
        tens_word = number_dict[ten_digit_isolated] #load value of number_dict[ten_digit_isolated] into tens_word
        ones_word = number_dict[ones_digit] #load value of number_dict[ones_digit] into ones_word
        final_word = tens_word + " " + ones_word #return final_word after construction

    elif ten_digit_isolated >=10 and ones_digit == 0:
        tens_word = number_dict[ten_digit_isolated] #load value of number_dict[ten_digit_isolated] into tens_word
        final_word = tens_word #return final_word after construction

    else: #not 10 or above, must be in the ones spot...
        tens_word = "" #tens_word not used. 
        ones_word = number_dict[ones_digit] #load value of number_dict[ones_digit] into ones_word
        final_word = ones_word #dump ones word into final_word for return
    return final_word #return final_word after construction

       

# ----------------------Final-Result------------------------------------ #
print(num_to_phrase(11)) #calls num_to_phrase and prints result
