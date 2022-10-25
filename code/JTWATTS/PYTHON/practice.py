###   *args and **kwargs
# blog_1 = "I do like the beats"
# blog_2 = "I'd like to travel more"
# blog_3 ="this is supeer awesome"
# lists = [1,2,3,4,5]
# def blogs(*args):
#     for element in args:
#         print(element)
# blogs(blog_1, blog_2, blog_3, list)

# blog_1 = "I do like the beats"
# blog_2 = "I'd like to travel more"
# blog_3 ="this is supeer awesome"
# lists = [1,2,3,4,5]
# def blogs(**kwargs):
#     for name in kwargs:
#         print(name, kwargs[name])
# blogs(alex='pop', joe='rock', jack='classic')


# blog_1 = "I do like the beats"
# blog_2 = "I'd like to travel more"
# blog_3 ="this is supeer awesome"
# lists = [1,2,3,4,5]
# def blogs(*args,**kwargs):
#     for variable in args:
#         print(variable)clear

#     for name in kwargs:    
#         print(name, kwargs[name])
# blogs(blog_3, blog_1, jack='classic')

book = open('C:\Users\cmd\Desktop\PDXBOOTCAMP\git_week_1\class_chihuahua\code\JTWATTS\PYTHON\test.txt')
contents = book.read()
print(contents)
book.close()



