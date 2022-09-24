from turtle import clear


class Person:
    
    def __init__(self,name,age):
        
        self.age = age
        self.name = name
    
       

    def display(self):
           print(self.age,self.name)
           return self.display
    def display_student(self):
            print(self.age,self.name,self)
            return self.display_students


Student=Person(12,'jack')
print(Student.age,Student.name)
    # def display(self):
        # return(f'{self.account_number},{self.name},{self.balance}' )


Me=Person(5,"young")      
print(Me.age,Me.name)  


# NewHire=Bank_Account()        
# print(NewHire.account_number,NewHire.name,NewHire.balance) 