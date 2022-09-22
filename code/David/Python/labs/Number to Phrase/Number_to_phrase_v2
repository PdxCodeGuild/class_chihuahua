from tkinter import N


while True:    
    num_to_phrase = (input("Give me a number: "))

    ones_dict = {
        1: 'one',
        2: 'two',
        3: 'three', 
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        0: 'zero'

    }

    teen_dict = {
        1: 'eleven',
        2: 'twelve',
        3: 'thirteen',
        4: 'fourteen',
        5: 'fifthteen',
        6: 'sixteen',
        7: 'seventeen',
        8: 'eighteen',
        9: 'nineteen'
    }

    tens_dict = {
        1: 'ten',
        2: 'twenty',
        3: 'thirty',
        4: 'fourty',
        5: 'fifthty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninty',
    }


    hundo = 'hundred'

    if len(num_to_phrase) == 1:
        output = ones_dict[int(num_to_phrase)]
    
    if len(num_to_phrase) == 2:
        if int(num_to_phrase[1]) == 0:
            output = tens_dict[int(num_to_phrase[0])]
        elif int(num_to_phrase[0]) == 1 and int(num_to_phrase[1]) >= 1:
            output = teen_dict[int(num_to_phrase[1])]
        elif int(num_to_phrase[0]) > 1 and int(num_to_phrase[1]) > 0:
            output = tens_dict[int(num_to_phrase[0])] + '-' + ones_dict[int(num_to_phrase[1])]
            
    if len(num_to_phrase) == 3:
        if int(num_to_phrase[1]) == 0 and int(num_to_phrase[2]) == 0:
            output = ones_dict[int(num_to_phrase[0])] + ' ' + hundo
        elif int(num_to_phrase[1]) == 1 and int(num_to_phrase[2]) >= 1:
            output = ones_dict[int(num_to_phrase[0])] + ' ' + hundo + ' ' + teen_dict[int(num_to_phrase[2])]
        elif int(num_to_phrase[1]) >= 1 and int(num_to_phrase[2]) == 0:
            output = ones_dict[int(num_to_phrase[0])] + ' ' + hundo + ' ' + tens_dict[int(num_to_phrase[1])]
        elif int(num_to_phrase[1]) >= 1 and int(num_to_phrase[2]) >= 1:
            output = ones_dict[int(num_to_phrase[0])] + ' ' + hundo + ' ' + tens_dict[int(num_to_phrase[1])] + '-' + ones_dict[int(num_to_phrase[2])]

    print(output)
