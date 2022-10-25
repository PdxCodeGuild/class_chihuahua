import requests
import string
response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
punctuation_removal = str.maketrans('', '', string.punctuation)
# print(response.text.lower().translate(punctuation_removal).split())

words = list(response.text.lower().translate(punctuation_removal).split())
words.sort(key=lambda tup: tup[0], reverse=True) 
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
