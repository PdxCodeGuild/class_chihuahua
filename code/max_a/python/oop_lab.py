class Bank_account():
    def __init__(self, number, full_name, initial_balance):
        self.account_no = number
        self.name = full_name
        self.balance = initial_balance
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew ${amount} from account.")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into account.")
    
    def display(self):
        print(f"Account details for Account #{self.account_no}:")
        print(f"Full Name: {self.name}")
        print(f"Current Balance: ${self.balance}")


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        return self.length*2 + self.width*2

    def area(self):
        return self.length * self.width
    
    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")
    
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section
    
    def display_student(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Section: {self.section}")