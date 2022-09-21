with open('hyde10.txt', 'r') as book:
    contents = book.read()
    #print(contents) #type str


    # words_counted = {

    # }

    lowercase_hyde = contents.lower()
    # print(lowercase_hyde)
    no_space = lowercase_hyde.split("' '.!?()--'")
    # no_space = str(no_space)
    print(no_space)
    # no_period = no_space.split(".!,?()--")
    # # no_period = str(no_period)
    # print(type(no_period))
    # no_comma = no_period.split(",")
    # no_comma = str(no_comma)
    # # print(no_comma)
    # no_exclam = no_comma.split("!")

    # def convert_to_str(ls):
    #     return str(ls)

    # def no_spaces():
    #     no_space = lowercase_hyde.split(" ")
    #     no_space = convert_to_str(no_spaces)
    #     return no_space
    # print(type(no_spaces()))

    # def no_periods():

    #     no_period = no_spaces.split(",!.?()--")
    #     no_period = convert_to_str(no_period)
    #     return no_period
    # print(no_periods())
        
    

    
    
    # def format_hyde():
    #     lowercase_hyde = contents.lower() #str
    #     no_space = lowercase_hyde.split(" ") #list
    #     no_space = str(no_space)
    #     no_period = no_space.split(".")
    #     no_comma = no_period
        
    # for char in no_space:
    #     no_period = no_space.split(".")
    #     no_period = str(no_period)
    # print(no_period)

    