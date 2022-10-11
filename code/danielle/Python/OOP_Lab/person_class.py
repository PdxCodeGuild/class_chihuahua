class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
            print(f"Your name is {self.name} and your age is {self.age}")
            
class Student(Person):
    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = section
    def display(self):
        print(f"Your name is {self.name}, age: {self.age}, in section: {self.section}")

display = Person("Danielle", 27)
display_student = Student("Danielle", 27, 1)

display.display()
display_student.display()
