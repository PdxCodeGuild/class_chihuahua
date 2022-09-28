
# define class
class Rectancle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #perimeter method
    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width

        
rectangle_1 = Rectancle(1,2)
rectangle_2 = Rectancle(30,5)
rectangle_3 = Rectancle(2,10)
rectangle_4 = Rectancle(10,25)

print(rectangle_3.perimeter())


#Rectangle Class
#Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
#Create a perimeter() method to calculate the perimeter of the rectangle and a area() method to calculate the area of ​​the rectangle.
#Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
#Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another volume() method to calculate the volume of the Parallelepiped.