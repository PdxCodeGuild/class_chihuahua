import requests

import requests
response = requests.get('https://www.gutenberg.org/cache/epub/1727/pg1727.txt')
response.encoding = 'utf-8' # set encoding to utf-8
print(response.text)

# word_dict is a dictionary where the key is the word and the value is the count
word_dict = {}
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])