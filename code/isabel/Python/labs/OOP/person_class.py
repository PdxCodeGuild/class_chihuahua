class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def display(self):
        return f"The person's name is: {self.name} and age: {self.age}"
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    def display_student(self):
        return f"This student's name is: {self.name}, age: {self.age} and course: {self.course}"

perp1 = Person('Johnny', 78)
print(perp1.display())
student1 = Student('Klaus', 22, "golfing")
print(student1.display())