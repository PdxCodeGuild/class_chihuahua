import re

with open('hyde10.txt', 'r') as book:
    contents = book.read()

    #print(contents) #type str


    # words_counted = {

    # }

lowercase_hyde = contents.lower()

# def format_hyde(str):

    

char = 0
while char <= len(lowercase_hyde) - 1:
    if lowercase_hyde[char].isnumeric() == True:
        lowercase_hyde = lowercase_hyde.replace(lowercase_hyde[char], '')
    else:
        char += 1
    # return lowercase_hyde

while char <= len(lowercase_hyde) - 1:
    if lowercase_hyde[char].isaplha() == False and lowercase_hyde[char].isspace() == False:
        lowercase_hyde = lowercase_hyde.replace(lowercase_hyde[char], '')
    else:
        char += 1
    # return lowercase_hyde

print(lowercase_hyde)



# print(format_hyde(contents))


pattern = r'\W+'
just_words = re.split(pattern, lowercase_hyde)
# print(type(just_words))
# print(just_words)


word_frequency = {}

for element in just_words:
    if element in word_frequency:
        word_frequency[element] += 1
    else:
        word_frequency[element] = 1
# print(word_frequency)

# def sort_this(dict):
sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

new_word_frequency = {}

for tup in sorted_word_frequency:
    tup[0], tup[1]
    for tup in enumerate(word_frequency):
        key = tup[0]
        value = tup[1]
        new_word_frequency[key] = value
print(new_word_frequency)

    
# print(sorted_word_frequency)



# word_frequency = {}

# for element in just_words:
#     if element in word_frequency:
#         word_frequency[element] += 1
#     else:
#         word_frequency[element] = 1


# print(word_frequency)





# # i = 0
# for word in just_words:
#     if just_words.isnumeric() == True:
#         just_words.remove(word)
#         print(just_words)
#         # return just_words



# just_words = p.findall(lowercase_hyde)
# print(just_words)






    # # print(lowercase_hyde)
    # no_space = lowercase_hyde.split(";")
    # no_space = str(no_space)
    # #no_space = no_space.splitlines(keepends=False)
    # print(no_space)
    #no_period = no_space.split(".!,?()--\'\\.\\;")
   # no_period = str(no_period)
   # print(no_period)
    # no_comma = no_period.split(",")
    # no_comma = str(no_comma)
    # # print(no_comma)
    # no_exclam = no_comma.split("!")

    # def convert_to_str(ls):
    #     return str(ls)

    # no_period = lowercase_hyde.split(".")
    # no_period = convert_to_str(no_period)
    # no_exclam = no_period.split("!")
    # no_exclam = convert_to_str(no_exclam)
    # no_qu = no_exclam.split("?")
    # no_qu = convert_to_str(no_qu)
    # no_l = no_qu.split(")")
    # no_l = convert_to_str(no_l)
    # no_r = no_l.split("(")
    # no_r = convert_to_str(no_r)
    # no_semi = no_r.split(";")
    # no_semi = convert_to_str(no_semi)
    # no_dash = no_semi.split("--")
    # no_dash = convert_to_str(no_dash)
    # no_quotes = no_dash.split("''""")
    # no_quotes = convert_to_str(no_quotes)
    # no_space_punct = no_quotes.split("' ")
    # no_space_punct = convert_to_str(no_space_punct)
    # no_space_puncts = no_space_punct.split("', ")
    # no_space_puncts = convert_to_str(no_space_puncts)
    # no_space_puncts_quotes = no_space_puncts.split(" ")
    # no_space_puncts_quotes = convert_to_str(no_space_puncts_quotes)
    # print(no_space_puncts_quotes)

    # # no_space_puncts_quotes.join("/")
    # # print(no_space_puncts_quotes.join("/"))

    # # def no_spaces():
    # #     no_space = lowercase_hyde.split(" ")
    # #     no_space = convert_to_str(no_spaces)
    # #     return no_space
    # # print(no_spaces())

    # # def no_periods():

    # #     no_period = no_spaces.split(".")
    # #     no_period = convert_to_str(no_period)
    # #     return no_period
    # # print(no_periods())
        
    

    
    
    # def format_hyde():
    #     lowercase_hyde = contents.lower() #str
    #     no_space = lowercase_hyde.split(" ") #list
    #     no_space = str(no_space)
    #     no_period = no_space.split(".")
    #     no_comma = no_period
        
    # for char in no_space:
    #     no_period = no_space.split(".")
    #     no_period = str(no_period)
    # print(no_period)

    