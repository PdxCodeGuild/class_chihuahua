#define class for person   
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return(f"Hello {self.name}, your age is {self.age}")

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def student_section(self):
        return(f"Hello {self.name}, your age is {self.age} and your section is {self.section}")



parent_1 = Person("Jeff",25)
parent_2 = Person("Mike",29)
parent_3 = Person("Ann",32)
student_1 = Student("Elliott",5, "Kindergarten")
student_2 = Student("Chloe",12, "7th Grade")
student_3 = Student("Elizabeth",9, "5th Grade")

print(parent_1.display_info())
print(parent_2.display_info())
print(parent_3.display_info())
print(student_1.student_section())
print(student_2.student_section())
print(student_3.student_section())

#Person Class
#Create a Python class Person with attributes: name and age of type string.
#Create a display() method that displays the name and age of an object created via the Person class.
#Create a child class Student which inherits from the Person class and which also has a section attribute.
#Create a method display_student() that displays the name, age and section of an object created via the Student class.