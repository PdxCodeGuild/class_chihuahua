import string
#import requests
#response = requests.get('https://www.gutenberg.org/cache/epub/1232/pg1232.txt')
#response.encoding = 'utf-8'
#print(response.text)


with open('the_prince.txt', 'r', encoding='utf-8') as file:
    book = file.read()
count_dict = {}    
def count_it(text):
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, '')
    text = text.split()
    #print(text)
    for word in text:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    text = list(count_dict.items())
    text.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(text))):
        print(text[i])
count_it(book)