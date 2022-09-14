word = "hello"
def string_compression(word):
    count = 0
    new_string =''
    for letter in range(len(word)):
        count+=1
        print(letter)
        if  letter + 1 >= len(word) or word[letter] != word[letter+1]:
            new_string+=word[letter] + str(count)
            count = 0
    print(new_string) 


string_compression(word)
        

