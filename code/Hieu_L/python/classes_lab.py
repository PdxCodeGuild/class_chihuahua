import random
import sys
class bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = random.randint(1111,9999)
    def __repr__(self):
         return str(f"balance: {self.balance} \nname: {self.name} \naccount number: {self.account_number}")

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdrawal(self, amount):
        self.balance -= amount
        return self.balance  

# account = bank_account("chase", 1000)
# account.deposit(100)
# print(account)
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
        self.perimeter = (2 * length) + (2 * width)
    def area(self):
        area = self.length * self.width 
        return area
    def perimeter(self):
        perimeter = (2 * self.length) + (2 * self.width)
        return perimeter
    def __repr__(self):
        area_ = self.area
        return str(f"rectangle dimensions: \nlength: {self.length} \nwidth: {self.width} \narea: {area_} \nperimeter: {self.perimeter}")

# shape = rectangle(22,66)
# print(shape)
# print(shape.perimeter)
class parallelepiped(rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        self.volume = length * width * height
    
    def volume(self):
        volume = self.height * self.length * self.width
        return volume

# shape = parallelepiped(22, 33, 44)
# print(shape.volume)
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return f"name: {self.name} \n age: {self.age}"
class student(person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section
    
    def display_student(self):
        return str(f"name: {self.name} \n age: {self.age} section: {self.section}")

# student1 = student("hieu", 99, "science")
# print(student1.display_student())