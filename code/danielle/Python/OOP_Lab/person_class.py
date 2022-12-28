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
<<<<<<< HEAD
display_student.display()
=======
display_student.display()
>>>>>>> 28a5ab8527a406c2de2ec6719bb2230bfeed4894
