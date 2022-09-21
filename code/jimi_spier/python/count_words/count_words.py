# Jimi Spier
# count_words.py
# 20220920
# ----------------------Import------------------------------------------ #
from string import punctuation as a_punc #import built-in string library. Grab puncuation and call it a_punc

# ----------------------File-Operations--------------------------------- #
with open("./Anguttaranikaya.txt", 'r') as file: # Open text file and call it file
    text = file.read() #assign variable to the file.read() fucntion and call it text
    

# ----------------------Processing-------------------------------------- #
    text = text.lower() # lowercase everything
    new_file = "" #empty string
    for chars in text: # loop through the text file and put each word into chars
        if chars not in a_punc: # if the chars(words) don't contain puncuation
            new_file = new_file + chars  # add the word to the new_file list
    list_file = new_file.split(" ") # split based on empty space 
    
    counted = {} #empty dict to dump key/values   
    for char in list_file:# loop through each word in text file
        if char in counted: # if a word in the list is found
            counted[char] += 1 #each new discovered word receives a 1, unless more are found then adds 1 to value
        else:
            counted[char] = 1 #if the word doesn't appear again, leave it at one
    sort_counted = sorted(counted.items(), key = lambda val : val[1], reverse=True) #takes lambda func to assign list to sorted tuple based on value reverse sorted
    
# ----------------------Final-Result------------------------------------ #

    print(sort_counted) # print the sorted word tuple list to console