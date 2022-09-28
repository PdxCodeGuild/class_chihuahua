import random
class bank_account:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        # self.account_number = random.randint(0,9)
    def __repr__(self):
        return print(f"account number: {self.account_number} \n name: {self.name} \n account number: {self.account_number}")

    def deposit(self, amount):
        # amount = input('enter deposit amount: ')
        self.balance += amount
        return self.balance
    
    def withdrawal(self, amount):
        # amount = input('enter withdrawal amount: ')
        self.balance -= amount
        return self.balance

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length * self.width 
        return area
    
    def perimeter(self):
        perimeter = (2 * self.length) + (2 * self.width)
        return perimeter

    def __repr__(self):
        return print(f"rectangle dimensions: \n length: {self.length} \n width: {self.width} \n area:")

class parallelepiped(rectangle):
    def __init__(self, height):
        self.height = height
    def volume(self):
        volume = self.height * self.length * self.width
        return volume

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return f"name: {self.name} \n age: {self.age}"

class student(person):
    def __init__(self, section):
        self.section = section
    def display_student(self):
        return f"name: {self.name} \n age: {self.age} section: {self.section}"
