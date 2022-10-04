# Jimi Spier
# rectangle_class.py
# 20220922

# ----------------------Class------------------------------------------- #

class Rectangle: 
    # ----------------------Constructor------------------------------------- #

    def __init__(self, length, width):      # Rectangle class construction initializer
        self.length = length                # Length constructor
        self.width = width                  # Width constructor

    # ----------------------Method------------------------------------------ #    
    
    def perimeter(self):
        # ----------------------Math-------------------------------------------- #
        p_meter = 2 * (self.length + self.width) #Calculate perimeter
        return p_meter                      #return to caller
    
    # ----------------------Method------------------------------------------ #    
    
    def area(self):
        # ----------------------Math-------------------------------------------- #
        a = self.length * self.width         #Calculate area 
        return a                             #return to caller
    
    # ----------------------Method------------------------------------------ #

    def parallelepiped(height):             #takes in one variable from outside
        poly1_base = Rectangle.area(poly1)  #Call Rectangle.area() method for poly1 and dump into poly1_base
        poly2_base = Rectangle.area(poly2)  #Call Rectangle.area() method for poly2 and dump into poly1_base
        # ----------------------Math-------------------------------------------- #
        poly1_answer = poly1_base * height  #Calculate parallelepiped for poly1
        poly2_answer = poly2_base * height  #Calculate parallelepiped for poly2
        
        # ----------------------Final-Result------------------------------------ #
        print(f"First parallelepiped based on poly1 is: {poly1_answer}")
        print(f"Second parallelepiped based on poly2 is: {poly2_answer}")

    # ----------------------Method------------------------------------------ #

    def display():                          #prints to console area and perimeter for each polygon
        # ----------------------Final-Result------------------------------------ #
        print()
        print(f"The Rectange one has an area of: {poly1.area()} and a perimeter of {poly1.perimeter()}\n")
        print(f"The Rectange two has an area of: {poly2.area()} and a perimeter of {poly2.perimeter()}\n")
    


poly1 = Rectangle(5,4)                      #Instantiation of poly1's details
poly2 = Rectangle(4,9)                      #Instantiation of poly2's details

Rectangle.display()                     # Calls display method
Rectangle.parallelepiped(8)             #calls method and inserts number to be used in calculation