class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width
    
    def display(self):
        return f'''
        Length:     {self.length}
        Width:      {self.width}
        Perimeter:  {Rectangle.perimeter(self)}
        Area:       {Rectangle.area(self)}'''

rectangle_1_length = int(input('Rectangle 1 Length: '))
rectangle_1_Width  = int(input('Rectangle 1 Width: '))

rectangle_2_length = int(input('Rectangle 2 Length: '))
rectangle_2_Width  = int(input('Rectangle 2 Width: '))


rectangle_1 = Rectangle(rectangle_1_length,rectangle_1_Width)
rectangle_2 = Rectangle(rectangle_2_length,rectangle_2_Width)

print(Rectangle.display(rectangle_1))
print(Rectangle.display(rectangle_2))

class Parallelepipede(Rectangle):
    
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def display_vol(self):
        return f'''
        Length: {self.length} 
        Width:  {self.width}
        Height: {self.height}
        volume: {Parallelepipede.volume(self)}'''

parallelepipede_1_length = int(input('Enter parallelepipede 1 Length: '))
parallelepipede_1_Width  = int(input('Enter parallelepipede 1 Width: '))
parallelepipede_1_Height = int(input('Enter Parallelepipede 1 Height: '))

parallelepipede_2_length = int(input('Enter parallelepipede 2 Length: '))
parallelepipede_2_Width  = int(input('Enter parallelepipede 2 Width: '))
parallelepipede_2_Height = int(input('Enter Parallelepipede 2 Height: '))


parallelepipede_1 = Parallelepipede(parallelepipede_1_length,parallelepipede_1_Width, parallelepipede_1_Height)
parallelepipede_2 = Parallelepipede(parallelepipede_1_length,parallelepipede_1_Width, parallelepipede_2_Height)

print(Parallelepipede.display(parallelepipede_1))
print(Parallelepipede.display(parallelepipede_2))