with open('hyde10.txt', 'r') as book:
    contents = book.read()
    print(contents) #type str


    # words_counted = {

    # }

    lowercase_hyde = contents.lower()
    # print(lowercase_hyde)
    for char in lowercase_hyde:
        no_space = lowercase_hyde.split(" ")
        no_space = str(no_space)
    print(no_space)
    for char in no_space:
        no_period = no_space.split(".")
        no_period = str(no_period)
    print(no_period)

    