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

while "" in word_list:
    word_list.remove("")

pair_dict = {}

index = -1
for word in word_list:
    if index < len(word_list) - 2: # the last word is not followed by any other words
        index += 1
        pair = (word, word_list[index+1])
        if pair in pair_dict:
            pair_dict[pair] += 1
        else:
            pair_dict[pair] = 1

most_used = list(pair_dict.items())
most_used.sort(key=lambda tup: tup[1], reverse=True)

for word_index in range(10):
    print(most_used[word_index])

