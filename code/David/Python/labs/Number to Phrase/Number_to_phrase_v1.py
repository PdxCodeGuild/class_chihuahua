while True:    
    num_to_phrase = input("Give me a number: ")

    ones_dict = {
        '1': 'one',
        '2': 'two',
        '3': 'three', 
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero'

    }

    teen_dict = {
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifthteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }

    tens_dict = {
        '10': 'ten',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'fourty',
        '50': 'fifthty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninty',
    }

    if int(num_to_phrase) < 10:
        output = ones_dict[num_to_phrase]
    elif int(num_to_phrase) == 10:
        output = tens_dict["10"]
    elif int(num_to_phrase) < 20:
        output = teen_dict[num_to_phrase]
    elif int(num_to_phrase) == 20:
        output = tens_dict["20"]
    elif int(num_to_phrase) > 20 and int(num_to_phrase) < 30:
        output = tens_dict["20"]+'-'+ones_dict[num_to_phrase[1]]
    elif int(num_to_phrase) > 30 and int(num_to_phrase) < 40:
        output = tens_dict["30"]+'-'+ones_dict[num_to_phrase[1]]
    elif int(num_to_phrase) > 40 and int(num_to_phrase) < 50:
        output = tens_dict["40"]+'-'+ones_dict[num_to_phrase[1]]
    elif int(num_to_phrase) > 50 and int(num_to_phrase) < 60:
        output = tens_dict["50"]+'-'+ones_dict[num_to_phrase[1]]
    elif int(num_to_phrase) > 60 and int(num_to_phrase) < 70:
        output = tens_dict["60"]+'-'+ones_dict[num_to_phrase[1]]
    elif int(num_to_phrase) > 70 and int(num_to_phrase) < 80:
        output = tens_dict["70"]+'-'+ones_dict[num_to_phrase[1]]
    elif int(num_to_phrase) > 80 and int(num_to_phrase) < 90:
        output = tens_dict["80"]+'-'+ones_dict[num_to_phrase[1]]
    elif int(num_to_phrase) > 90 and int(num_to_phrase) < 100:
        output = tens_dict["90"]+'-'+ones_dict[num_to_phrase[1]]
    



    print(output)

    