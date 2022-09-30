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
    def init(self, length, width, height):
        super().init(length, width)
        self.height = height
    def volume(self):
        return self.area * self.height

'''
notes from alex on github.

class Rabbit(Animal):
def init(self, legs, color, speed): ##adding the new attribute speed
super().init(legs, color) ## referencing old attributes legs,color
self.speed = speed
'''