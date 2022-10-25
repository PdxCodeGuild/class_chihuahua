"""
OOP or Object Oriented Programming
Classes
1) create a class
2) Method and properties
3) Instantiate a class, by creating an object
4) Every class can have attributes and methods.  Attributes are propertiesd
('red',)
properties are
to create a class you have to use the key work class
after you create a class, you have to initiate it
"""
class Employee:
    pass
# This is how you initiate a class
empl_1 = Employee()
empl_2 = Employee()
empl_1.first= "name"
empl_1.last = "Last"
empl_1.pay = 50
empl_1.email = 'myemail@address'

empl_1.first= "name2"
empl_1.last = "Last2"
empl_1.pay = 150
empl_1.email = 'myemail@address2'
print(empl_1.first)
class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last=last
        self.pay=pay
        self.email = first+"." + last + "@gmail.com"
    def fullname(self):
        return self.first + " " + self.last
empl_1=Employee('first','middle',50)
empl_1=Employee('first2','middle2',50)
print(empl_2.first)
      