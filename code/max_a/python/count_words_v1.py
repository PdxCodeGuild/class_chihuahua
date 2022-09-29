from xml.dom.minidom import CharacterData
import requests

punctuations = ['.', '?', ',', '!', '\n', '\r', '-', '—', '"', '“', '”', '’s']

response = requests.get('https://www.gutenberg.org/cache/epub/64317/pg64317.txt')
response.encoding = 'utf-8'
book = response.text
book = book[book.find("In "):book.find("the past.") + 9]

with open('.\\code\\max_a\\the_great_gatsby.txt', 'w', encoding='utf-8') as file:
    file.write(book)

depunct_book = book.lower()
for punct_char in punctuations:
    depunct_book = depunct_book.replace(punct_char, " ")
word_list = depunct_book.split(" ")

word_dict = {}

for word in word_list:
    if word == "" or word == " ":
        pass
    else:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
        
most_used = list(word_dict.items())
most_used.sort(key=lambda tup: tup[1], reverse=True)

for word_index in range(10):
    print(most_used[word_index])
