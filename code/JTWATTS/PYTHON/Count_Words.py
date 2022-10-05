import requests
from collections import Counter


alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# response = requests.get('https://www.gutenberg.org/files/57585/57585-0.txt')
# book = response.text
# # book = book.strip(' ')
# seperate=(' ')
# book = book.lower()
# print(len(book))
with open('books.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text=text.replace("."," ")
    text=text.replace(":/"," ")
    text=text.replace("\\"," ")
    text=text.replace("_"," ")
    text=text.replace("-"," ")
    text=text.replace("["," ")
    text=text.replace("]"," ")
    text=text.replace("\n"," ")
    text=text.split(" ")
    # print(text.counter())
    keey=set((text))
    # print(set((text)))
    # for x in text:
    #     print(keey[x]+text[x])
    counting= [[text.count(word), word] for word in set(text)]
    # print(counting)
    top_ten = counting.sort()
   
    print(top_ten)
    print(counting)
    
    # print(type(counting))
# counting = Counter()
# for counter in text:
#     counting [text] +=1
# print(counting.most_common(10))    

    words = counting
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    
    # print(text.most_common(1))
#     i = 0
# while i < len(text):
#   sorttext={}
#   print(text[i])
#   sorttext.append{}

#   i = i + 1

# my_ticket = text
# random_ticket = text

# # for x in range(0,4)
# counter = 0
# for char in my_ticket:
#   if char in my_ticket:
#     print("we have match", char)
#     counter+=1    

# names: text = ['Bob', 'Mark', 'Jack']

# def list_summation(lst: List[int]) -> int:
#     return sum(lst)