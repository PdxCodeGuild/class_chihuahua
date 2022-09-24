'''
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
Create a perimeter() method to calculate the perimeter of the rectangle and a area() method to calculate the area of ​​the rectangle.
Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another volume() method to calculate the volume of the Parallelepiped.
'''

# created class 'Rectangle' and assigned length and width attributes.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # defined perimeter method to calculate the perimeter distance of the rectangle
    def perimeter(self):
        return (self.length + self.width) * 2

    # defined the area method to calculate the area of the rectangle
    def area(self):
        return self.length * self.width
    
    # defined the display method to return the length, width, perimeter, and area values
    def display(self):
        return f"Length: {self.length} Width: {self.width} Perimeter:  {Rectangle.perimeter(self)} Area:  {Rectangle.area(self)}"

# created two instances of Rectangle with length and width
rectangle_1 = Rectangle(5, 8)
rectangle_2 = Rectangle(12, 20)

# use print and the display method to display the length, width, perimeter, and area of the rectangle_1 and rectangle_2
print(Rectangle.display(rectangle_1))
print(Rectangle.display(rectangle_2))

# created new class Parallelepipede that is a "child" of class Rectangle and inherits the lenght and width attributes from Rectangle
class Parallelepipede(Rectangle):
    # added a new attribute 'height' that does not apply to the parent, Rectangle
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    # defined new method, volume, that multiplies length by width by height in order to calculate the volume of parallelepipede
    def volume(self):
        return self.length * self.width * self.height

    # defined a new display method to return the length, width, height, and volume values
    def display_vol(self):
        return f"Length: {self.length}  Width: {self.width}  Height: {self.height}  volume: {Parallelepipede.volume(self)}"

# instantiated two instances of Parallelepipede
parallelepipede_1 = Parallelepipede(5, 8, 4)
parallelepipede_2 = Parallelepipede(12, 20, 5)

# use print and the display.vol method to display the length, width, height, and volume of parallelepipede_1 and parallelepipede_2
print(Parallelepipede.display_vol(parallelepipede_1))
print(Parallelepipede.display_vol(parallelepipede_2))
