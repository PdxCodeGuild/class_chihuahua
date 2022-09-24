class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        display = f'''
        The persons name is {self.name} and they are {self.age} years old.
        '''
        return display
    
class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age) # referencing old attributes attributes
        self.section = section

    def display_student(self):
        display = f'''
        The persons name is {self.name}, they are {self.age} years old and is in the {self.section} section.
        '''
        return display

jordan = Student("Jordan", 26, "Computer Science") #creating an instance of the class
print(jordan.display_student())