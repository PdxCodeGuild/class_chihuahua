
class Rectangle:
    
    def __init__(self,lenght,width):
        
        self.lenght = lenght
        self.width = width
        
       

    def perimeter(self):
            self.perimeter=self.lenght *2 +self.width *2
           
            return self.perimeter
    def area(self):
            self.area=self.lenght * self.width
           
            return self.area   
   


display=Rectangle(12,14)      

class Parallelepipede(Rectangle):
    def __init__(self,lenght,width,height):
        super().__init__(lenght,width)#super is referencing old attributes from rectangel
        self.height = height
    def volume(self):
         self.volume=self.lenght *2 +self.width *2+ self.height *2
         return self.volume
#attribute
#method

vol=Parallelepipede(12,14,5)

        
print(display.lenght,display.width) 
print(display.perimeter(),display.area())
print(vol.lenght,vol.width,vol.height) 
print(vol.perimeter(),vol.area(),vol.volume())
#test

