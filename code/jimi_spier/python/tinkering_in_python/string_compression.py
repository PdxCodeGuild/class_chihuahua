word = "aabeeteeyylhlllnb"



def string_compression(word):
    count = 0 #initialize count with zero for loop entry
    
    new_string ='' # initialize new string with empty data
    
    for letter in range(len(word)): 
        # range(len(word)) is the length of the string as the range of numbers. 
        # letters is a numerical position holder 
      
        count+=1 #Adds one to count before processing.
        
    
        if  letter + 1 >= len(word) or word[letter] != word[letter+1]: 
    # [letter + 1 >= len(word)]        = Stops if statement if out of bounds
    # [word[letter] != word[letter+1]] = compares current position letter with future(+1) letter to see if same. 
    #                                    Return True if numbers don't match
    #  or Operation                    = one side OR the other has to pass to continue script. 
            new_string+=word[letter] + str(count) # constructs new string with word at position letter and count as a string
            count = 0 #zeros out count for next iteration 
            
        
    return(new_string) #returns newly constructed string with character counts

print(string_compression(word))