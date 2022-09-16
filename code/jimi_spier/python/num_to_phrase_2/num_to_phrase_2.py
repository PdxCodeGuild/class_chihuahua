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
        100:"hundred"
    } #dictionary of available keys and values

       # ----------------------Math-------------------------------------------- #
    tens_digit = num // 10 #floor division to isolate tens position as single int
    ten_digit_isolated = tens_digit * 10 # after getting tens position number, multiply by ten to reconstitute
    ones_digit = num % 10 # modulus removes tens and reveals ones value

    tens_word = "" #initialize variable 
    ones_word = "" #initialize variable 
    # ----------------------Processing-------------------------------------- #
    if num > 0 and num < 21:#if the number is between 1 and 19 return value to console
        return number_dict[num] #load value of number_dict[num] and returns to console
    elif num >= 21 and num < 100:       
        tens_digit = num // 10 #floor division to isolate tens position as single int
        ten_digit_isolated = tens_digit * 10 # after getting tens position number, multiply by ten to reconstitute
        ones_digit = num % 10
        if ones_digit == 0:
            tens_word = number_dict[ten_digit_isolated]
            final_word = tens_word               
        else:
            tens_word = number_dict[ten_digit_isolated]
            ones_word = number_dict[ones_digit]
            final_word = tens_word + " " + ones_word
    elif num == 100:
       hundreds = ten_digit_isolated // 100
        #hundred_ones_digit = hundreds % 100
       hundreds_place = number_dict[100]
       hundreds_left_position = number_dict[hundreds]
       final_word = hundreds_left_position + " " + hundreds_place
    elif num >= 101 and num < 1000:
        hundreds = tens_digit // 10 #break off left most number
        hundred_ones_digit = num % 100
        if hundred_ones_digit >=20 and hundred_ones_digit < 100:
            new_tens = (hundred_ones_digit // 10) * 10
            new_ones = hundred_ones_digit % 10
            hundreds_left_position = number_dict[hundreds]
            hundreds_place = number_dict[100]
            tens_place = number_dict[new_tens]
            ones_place = number_dict[new_ones]
            final_word = hundreds_left_position + " " + hundreds_place + " " + tens_place + " " + ones_place #final_word construction
        else:
            hundreds_left_position = number_dict[hundreds]
            hundreds_place = number_dict[100]
            ones_word = number_dict[hundred_ones_digit]
            final_word = hundreds_left_position + " " + hundreds_place + " " + ones_word #final_word construction
    else:
        print("error")   # catch all error 
        
    return final_word #collect final_word from if statements and send back to console


       

# ----------------------Final-Result------------------------------------ #
for user_input in range(5,100, 1): #using range() for debugging purposes
    print(num_to_phrase(user_input)) #calls num_to_phrase and prints result
