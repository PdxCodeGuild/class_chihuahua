import string
punctuation = string.punctuation #cleaning up punctuation

with open('labtext.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    #print(text)
    #text = text.split()

# lower casing all words and removing punctuation
for char in punctuation:
    text = text.replace(char, ' ')
text = text.lower()

word_list = text.split()
# # # creating the dictionary
table_of_words = {}
for word in word_list: # count occurences of a word in a dictionary
    if word in table_of_words:
        table_of_words[word] += 1
    else:
        table_of_words[word] = 1

d = list(table_of_words.items()) # .items() returns a list of tuples
d.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(table_of_words))):  # print the top 10 words, or all of them, whichever is smaller
     print(d[i])
