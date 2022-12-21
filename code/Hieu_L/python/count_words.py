import requests
import string

response = requests.get('https://www.gutenberg.org/cache/epub/6130/pg6130.txt')
response.encoding = 'utf-8' # set encoding to utf-8
text = str(response.text.lower())
punc = string.punctuation
stripped_text = ""
for word in text: 
    if word not in punc:
        stripped_text += word
split_text = stripped_text.split()
dict_text = {}
for word in split_text:
    if word not in dict_text:
        dict_text[word] = 1
    else:
        dict_text[word] += 1
word_dict = dict_text
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])