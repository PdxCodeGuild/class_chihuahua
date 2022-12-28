

class Person:
    
    def __init__(self,name,age):
        
        self.age = age
        self.name = name
    
       

    def display(self):
           print(self.age,self.name)
           return self.display
    

class Student(Person):
    def __init__(self,age,name,section):
        super().__init__(age,name)
        self.section = section
    def display_student(self):
        self.display_student=print(self.age,self.name,self.section)


new_guy=Student(12,'jack','coder')

print(new_guy.age,new_guy.name,new_guy.section)
    # def display(self):
        # return(f'{self.account_number},{self.name},{self.balance}' )


Me=Person(5,"young")      
print(Me.age,Me.name)  


# NewHire=Bank_Account()        
# print(NewHire.account_number,NewHire.name,NewHire.balance) 