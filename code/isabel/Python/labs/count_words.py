
import re

with open('hyde10.txt', 'r') as book:
    contents = book.read()

   
lowercase_hyde = contents.lower()

def format_hyde(lowercase_hyde):
    
    char = 0

    while char <= len(lowercase_hyde) - 1:
        if lowercase_hyde[char].isalpha() == False and lowercase_hyde[char].isspace() == False:
            lowercase_hyde = lowercase_hyde.replace(lowercase_hyde[char], '')
        else:
            char += 1
    return lowercase_hyde


lowercase_hyde_formatted = format_hyde(lowercase_hyde)
def seperate_format(lowercase_hyde):


    pattern = r'\W+'
    just_words = re.split(pattern, lowercase_hyde)
    return just_words

print(seperate_format(lowercase_hyde_formatted))


just_words = seperate_format(lowercase_hyde)
def create_dictionary(just_words):
    word_frequency = {}

    for element in just_words:
        if element in word_frequency:
            word_frequency[element] += 1
        else:
            word_frequency[element] = 1
    return word_frequency

print(create_dictionary(just_words))


word_frequency = create_dictionary(just_words)
def sort_this(dict):
    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    new_word_frequency = {}

    for tup in sorted_word_frequency:
        tup[0], tup[1]
        for tup in enumerate(word_frequency):
            key = tup[0]
            value = tup[1]
            new_word_frequency[key] = value
    return new_word_frequency

print(sort_this(word_frequency))

new_word_frequency = sort_this(word_frequency)
word_freq_items = list(new_word_frequency.items())
word_freq_items.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(word_freq_items))):
    print(word_freq_items[i])



    



    