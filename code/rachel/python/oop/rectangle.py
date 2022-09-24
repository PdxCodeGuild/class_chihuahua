'''
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
Create a perimeter() method to calculate the perimeter of the rectangle and a area() method to calculate the area of ​​the rectangle.
Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another volume() method to calculate the volume of the Parallelepiped.
'''

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width
    
    def display(self):
        return f"Length: {self.length} Width: {self.width} Perimeter:  {Rectangle.perimeter(self)} Area:  {Rectangle.area(self)}"

rectangle_1 = Rectangle(5, 8)
rectangle_2 = Rectangle(12, 20)

print(Rectangle.display(rectangle_1))
print(Rectangle.display(rectangle_2))