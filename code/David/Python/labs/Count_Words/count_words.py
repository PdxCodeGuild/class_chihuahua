

word_dict = {

}

word_list = []
top10 = []



with open ('C:/Users/lug_n/Desktop/git/class_chihuahua/code/David/Python/labs/Count_Words/gatsby.txt' , 'r', encoding='utf-8') as file:
    text = file.read()
    word_list = text.split(' ')
    for word in word_list:
        if word not in word_dict:
            word_dict.update({f'{word}':1})
        elif word in word_dict:
            word_dict[word] += 1

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

# for key, value in word_dict.items():
#     print(key, value)        
        






