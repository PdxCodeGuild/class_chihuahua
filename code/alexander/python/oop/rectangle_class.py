class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
    def area(self):
        return self.length * self.width
    def display(self):
        print(self.length, self.width, self.perimeter, self.area)
class parallelepipede(rectangle):
    def __init_(self, height):
        self.height = height
    def volume(self):
        return self.area * self.height