numbers_class = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
    11: 'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
    20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60: 'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'one hundred',
    200:'two hundred', 300:'three hundred', 400:'four hundred', 500:'five hundred', 600:'six hundred', 700:'seven hundred', 800:'eight hundred', 900:'nine hundred'}



def num_to_phrase(num):
    try:
        return numbers_class[num]
    except KeyError:
        try:
            ones_value = num % 10
            tenths_value = num - ones_value
            return numbers_class[tenths_value] + ' ' + numbers_class[ones_value]
        except KeyError:
            ones_value = num % 10
            tenths_value = num % 100
            hundreths_value = num - tenths_value
            if tenths_value <= 19:
                return numbers_class[hundreths_value] + ' ' + numbers_class[tenths_value]
            else:
                tenths_value = tenths_value - ones_value
                return numbers_class[hundreths_value] + ' '+ numbers_class[tenths_value] + ' ' + numbers_class[ones_value]
   
# print(527 % 10)
print(num_to_phrase(650))
# print(num_to_phrase(8))
