
import requests


response = requests.get('https://www.gutenberg.org/files/105/105-0.txt')
response.encoding = 'utf-8'

# assign variable to hold text
text = response.text
# convert all text to lowercase letters
text = text.lower()
# assign punctuation to variable 'punctuation'
punctuation = """!()-[]{};:'"\<>,./?@#$%^&*_~"""

# iterate through 'text' to remove punctuation.
for ele in text:
    if ele in punctuation:
        text = text.replace(ele, "")

# convert 'text' into a list separated by spaces.
text = text.split(" ")

# define a function to count the words in 'text' by creating an empty dictionary and iterating through the text, adding each new word to the dictionary as a key with the number of occurrences as the value. 
def count_words(text):
    count = dict()

    for word in text:
        if word in count: #if the word is in the dictionary, add 1 to the value
            count[word] += 1 
        else:  #if the word isn't in the dictionary, add word with value of 1
            count[word] = 1
    
    return count # return the the dictionary 

word_dict = count_words(text) 

words = list(word_dict.items())
words.sort(key = lambda tup: tup[1], reverse=True)

# print the 10 most used words in the text
for i in range (min(10, len(words))):
    print(words[i])
