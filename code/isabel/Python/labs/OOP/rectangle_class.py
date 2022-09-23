class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return self.length * 2 + (self.width * 2)
    def area(self):
        return self.width * self.length
    def display(self):
        return f"This rectangle has length: {self.length}, width: {self.width}, perimeter: {self.perimeter()} and area: {self.area}"

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        return self.length * self.height * self.width

big_rectangle = Rectangle(4, 6)
print(big_rectangle.area())
big_box = Parallelepipede(4, 6, 7)
print(big_box.volume())
