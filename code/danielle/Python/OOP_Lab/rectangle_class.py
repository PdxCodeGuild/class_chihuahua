class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def perimeter(self):
        perimeter = 2 * ((self.length) + (self.width))
        print(f"perimeter = {perimeter}")
    def area(self):
        area = (self.length) * (self.width)
        print(f"area = {area}")


class Parallelepipede(Rectangle):
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
    def volume(self):
        volume = (self.width * self.length) * self.height
        print(f"volume = {volume}")
        
display = Rectangle(5, 6)
display = Parallelepipede(5, 6, 2)

display.area()
display.perimeter()
display.volume()
