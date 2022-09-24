from xml.dom.minidom import CharacterData
import requests

chosen = input("Please choose a word: ")

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

following_list = {}

index = -1
for word in word_list:
    if word == chosen:
        following = word_list[index + 1]
        if following in following_list:
            following_list[following] += 1
        else:
            following_list[following] = 1

most_following = list(following_list.items())
most_following.sort(key=lambda tup: tup[1], reverse=True)

for word_index in range(10):
    print(most_following[word_index])

# this file is currently under construction while I try to figure out what's wrong with it
