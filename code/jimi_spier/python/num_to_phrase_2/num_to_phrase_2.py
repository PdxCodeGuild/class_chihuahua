# Jimi Spier
# num_to_phrase_2.py
# 20220915


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
        if ones_digit == 0:#if the the number ends in zero
            tens_word = number_dict[ten_digit_isolated] #grab tens_digit value from dict
            final_word = tens_word               
        else:#if the rest of the number do not end in zero
            tens_word = number_dict[ten_digit_isolated] #grab tens_digit value from dict
            ones_word = number_dict[ones_digit] #grab ones_digit value from dict
            final_word = tens_word + " " + ones_word #final_word construction

    elif num == 100: # if the number equals 100
       hundreds = ten_digit_isolated // 100 #break off left most number
        #hundred_ones_digit = hundreds % 100
       hundreds_place = number_dict[100] #hundreds placeholder
       hundreds_left_position = number_dict[hundreds] # grabs left most position from dict
       final_word = hundreds_left_position + " " + hundreds_place #final_word construction


    elif num >= 101 and num < 1000:# if num is greater than or equal to 101 and less than 1000
        hundreds = tens_digit // 10 #break off left most number
        hundred_ones_digit = num % 100 # break of right-most digit
        if hundred_ones_digit >=20 and hundred_ones_digit < 100: # if the tens digit is between 20 and 99
            new_tens = (hundred_ones_digit // 10) * 10 #isolate "tens" spot and re-constitute
            new_ones = hundred_ones_digit % 10 #user modulus to drop left position numbers
            hundreds_left_position = number_dict[hundreds] #places left most digit from dict
            hundreds_place = number_dict[100] #hundreds placeholder
            tens_place = number_dict[new_tens] #places tens digit from dict
            ones_place = number_dict[new_ones] #places ones digit from dict
            final_word = hundreds_left_position + " " + hundreds_place + " " + tens_place + " " + ones_place #final_word construction
        else:
            hundreds_left_position = number_dict[hundreds] #places left most digit from dict 
            hundreds_place = number_dict[100] #hundreds placeholder
            ones_word = number_dict[hundred_ones_digit] #places ones digit from dict 
            final_word = hundreds_left_position + " " + hundreds_place + " " + ones_word #final_word construction
    else:
        print("error")   # catch all error 
    return final_word #collect final_word from if statements and send back to console

# ----------------------Final-Result------------------------------------ #
for user_input in range(1,1000): #using range() for debugging purposes
    print(num_to_phrase(user_input)) #calls num_to_phrase and prints result
