class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)

    def area(self):
        return self.length * self.width
    
    def display(self):
        display = f''' 
        The rectangle legth is: ", {self.length}
        The rectangle width is: ", {self.width} 
        The rectangle perimeter is: ", {self.perimeter()}
        The rectangle area is: ", {self.area()}
        '''
        return display

class Parallelepipede(Rectangle):
    def __init__(self, length, width , height):
        super().__init__(length, width) # referencing old attributes attributes
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

print(Rectangle(200, 100).display())
#testing git