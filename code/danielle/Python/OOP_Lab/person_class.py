class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        def display():
            print(f"Your name is {name} and your age is {age}")
        display()

class Student(Person):
    def __init__(self):
