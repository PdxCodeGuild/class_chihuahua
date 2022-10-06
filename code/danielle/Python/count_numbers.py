import requests
import string
response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
punctuation_removal = str.maketrans('', '', string.punctuation)
print(response.text.lower().translate(punctuation_removal))
