class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f'''
        Name: {self.name}
        Age:  {self.age}
        ''')

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def display_section(self):
         print(f'''
        Name: {self.name}
        Age:  {self.age}
        Sec:  {self.section}
        ''')

person_1 = Student('David', 32, 1337)
person_2 = Student('Bob', 31, 5377)


while True:

    selection = int(input('''
    1. Person 1
    2. Person 2

    '''))
    if selection == 1:
        print(person_1.display_section())
    elif selection == 2:
        print(person_2.display_section())