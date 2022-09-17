from re import M


def num_to_phrase(num):
    numbers_class = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
    return numbers_class[num] 
pass
   
print(num_to_phrase(8))
