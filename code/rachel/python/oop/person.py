'''
Create a Python class Person with attributes: name and age.
Create a display() method that displays the name and age of an object created via the Person class.
Create a child class Student which inherits from the Person class and which also has a section attribute.
Create a method display_student() that displays the name, age and section of an object created via the Student class.
'''
# Created new class Person with attributes name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # created display method to display name and age.
    def display(self):
        return f"Name: {self.name}  Age: {self.age}"

# instantiated two instances of class Person
person_1 = Person("Jane Doe", 32)
person_2 = Person("John Doe", 23)

# use print and display to display name and age for the objects of the Person class
print(Person.display(person_1))
print(Person.display(person_2))

# created new class Student that inherits the attributes of the Person class (name, age), but also has it's own attribute, section.
class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    # created display_student method to display the name, age, and section for objects of the Student class
    def display_student(self):
        return f"Student Name: {self.name}  Student Age: {self.age}  Section: {self.section}"

# Instantiated objects of the Student class
student_1 = Student("Sadie", 15, 123)
student_2 = Student("Ben", 14, 456)

# use print and display_student method to display the name, age, section for specified objects of the Student class
print(Student.display_student(student_1))
print(Student.display_student(student_2))