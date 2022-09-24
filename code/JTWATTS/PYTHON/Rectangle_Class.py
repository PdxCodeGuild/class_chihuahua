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
   
    # def display(self):
        # return(f'{self.account_number},{self.name},{self.balance}' )
    # def Parallelepipede(self):    

display=Rectangle(12,14)      



# NewHire=Bank_Account()        
print(display.lenght,display.width) 
print(display.perimeter(),display.area())

