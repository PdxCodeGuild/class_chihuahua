class Bank_Account:
    
    def __init__(self,account_number,name,balance):
        
        self.account_number = account_number
        self.name = name
        self.balance = balance
       

    def deposits(self):
            
            self.balance+=20
            return self.balance
    def withdrawal(self):
            
            self.balance -= 10
            return self.balance    
   
    # def display(self):
        # return(f'{self.account_number},{self.name},{self.balance}' )
NewHire=Bank_Account(12345678,'Tom',200)      

# NewHire=Bank_Account()        
print(NewHire.account_number,NewHire.name,NewHire.balance) 
for money_in in range(0,1):
    print(NewHire.deposits())
   
for money_out in range(0,1):
    print(NewHire.withdrawal())   



