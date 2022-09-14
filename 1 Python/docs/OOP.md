## Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data:

Classes are a way to structure data in a way that is easy to manage and easy to build upon. By data I mean attributes and methods. A method is a function related to a class. Attributes are values.

A class is a user-defined blueprint or prototype from which objects are created. Creating a new class creates a new type of object, allowing new instances of that type to be made. An Object is an instance of a Class. 


## Classes - instantiation

```python
class Employee:
      pass
empl_1 = Employee()
empl_2 = Employee()
```

The class Employee is the blueprint, and empl_1 & empl_2 are *instances* of that class. If you remember I mentioned that everything is an **object** in Python. A dictionary, an integer, a boolean are all instances of classes. When we make a list using `[]` syntax, we are instantiating a new instance of the **List** class. 

```Python
print(type([]))
#returns <class 'list'>
```

## Classes - attributes

Let's start building our model:

```python
class Employee:
 pass
 
empl_1 = Employee()
empl_2 = Employee()
 
empl_1.first = 'Alex'
empl_1.last = 'D'
empl_1.pay = 50
empl_1.email = 'alex.d@gmail.com'
 
 
empl_2.first = 'Bruce'
empl_2.last = 'Wayne'
empl_2.pay = 200
empl_2.email = 'batman@gmail.com'
 
print(empl_1.first, empl_2.first )
```

How inefficient is this method? A lot! If we had 50 employees, we would need to repeat the process several times. But there's a better way!


```python
class Employee:
    def __init__(self, first,last ,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
 
empl_1 = Employee('alex', 'd', 50)
empl_2 = Employee('Bruce', 'Wayne', 60)
 
print(empl_1.email, empl_2.email )
```

__init__ is a python "magic method"; it identifies a special kind of function called a constructor. Constructors are used to create class instances. So, when we define an __init__ method on a class, we can specify exactly how that class gets created. 

## Methods

**Classic Method**

Methods are functions within your class:

```python
class Employee:
    def __init__(self, first,last ,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
    def fullname(self):
        return self.first + ' ' + self.last
 
 
print(empl_1.fullname())
```
Let's have a look at some methods:

**Class Method**

Class methods do not take the instance as first arguments. They take the class

```python
class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def fullname(self): # instance method
       # instance object accessible through self
        return "%s %s" % (self.name, self.surname)
    
    @classmethod
    def allowed_titles_starting_with(cls, startswith): # class method
       # class or instance object accessible through cls
       return [t for t in cls.TITLES if t.startswith(startswith)]
 
 
print(Person.allowed_titles_starting_with("M"))
```

What are class methods good for? Sometimes there are tasks associated with a class which we can perform using constants and other class attributes, without needing to create any class instances. If we had to use instance methods for these tasks, we would need to create an instance for no reason, which would be wasteful. 

**Static Method**

Static methods do not take the instance or the class

```python
import requests
class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_data():
        data = requests.get('https://jsonplaceholder.typicode.com/users')
        response = data.json()
        return response

person = Person('alex')
print(person.get_data())
```

## Inheritance

Inheritance allows us to inherit attributes and methods from a parent class. We can override or create new functionality without affecting the parent class

```python
class Animal:
    def __init__(self, legs, color):
        self.legs = legs
        self.color = color
    
    def make_sound(self):
        print(f"I am a {self.legs} legged {self.color } animal!")

#Use the Animal class to create an object, and then execute the make_sound method:

class Rabbit(Animal):
    def say_hello(self):
        print('I am a cute rabbit')

elephant = Animal("4", "grey")
elephant.make_sound()
rabbit = Rabbit("2", "white")
rabbit.make_sound() ##the rabbit class inherited the make_sound method
rabbit.say_hello()
```

**override methods and add attributes with super()__**

```python
class Animal:
  def __init__(self, legs, color):
    self.legs = legs
    self.color = color
  def make_sound(self):
    print(f"I am a {self.legs} legged {self.color } animal!")
# adding the init and super methods, so we can add additional attributes
class Rabbit(Animal):
    def __init__(self, legs, color, speed): ##adding the new attribute speed
        super().__init__(legs, color) ## referencing old attributes legs,color
        self.speed = speed
    ## overriding the make_sound method
    def make_sound(self):
        print(f'sqeeeeek!! I am running at {self.speed} miles per hour')
    
    ## defining a new method only for Rabbit
    def say_hello(self):
        print('I am a cute rabbit')
        
elephant = Animal("4", "grey")
elephant.make_sound()
rabbit = Rabbit("2", "white", 10)
rabbit.make_sound()
rabbit.say_hello()
```

## 4 Pillars of OOP

## Encapsulation 

It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variable. 

```python
class Account:
    def __init__(self):
        # Protected member using double underscore __ 
        self.__balance = 0
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        print( f'current balance is { self.__balance} ' )
    def withdraw(self, amount):
        if amount > self.__balance:
            print( 'not enough funds' )
        else:
            self.__balance -= amount
alex_account = Account()
alex_account.deposit(1000)
print(alex_account.__balance) ##will trow an error
## You can still access the variable using the following syntax: instance._class__attribute
```

## Abstraction

Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function, but inner working is hidden. 

In this example we're exposing to the end user only one main method, which is `send_mail`. The other methods are private and can not be accessed externally. 

```python
class Mail_sender:
    def __init__(self):
        pass
    def send_mail(self):
        self.__connect()
        self.__authenticate()
        self.__disconnect()
    def __connect(self):
        print('connecting')
    def __disconnect(self):
        print('disconnecting')
    def __authenticate(self):
        print('authenticating')
outlook= Mail_sender()
print(outlook.send_mail())
```

## Inheritance

Inheritance is a mechanism that allows us to reuse code. See examples above.

## Polymorphism

Polymorphism in Python allows us to define methods in the child class with the same name as defined in their parent class. The process of re-implementing a method in the child class is known as Method Overriding.


```python
class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")

bird = Bird()
parrot = parrot()
penguin = penguin()

bird.intro()
bird.flight()
 
parrot.intro()
parrot.flight()
 
penguin.intro()
penguin.flight()
```