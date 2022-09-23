
# Jimi Spier
# bank_account_class.py
# 20220922


class Bank_account: 
    # ----------------------Constructor------------------------------------- #

    def __init__(self, account_number, name, balance): #Class construction initializer 
        self.account = account_number                   #Account_number constructor
        self.name = name                                #Name constructor
        self.balance = balance                          #Balance constructor

    # ----------------------Function---------------------------------------- #
    
    def deposit(self, deposit_amt): #Method will add funds to balance based on deposit_amt
        self.deposit_amt = deposit_amt #Setting up the variable deposit_amt
        new_amt = deposit_amt + self.balance #Adding deposit_amt to self.balance and storing it in new_amt
        self.balance = new_amt # dumping value from new_amt into self.balance
        return self.balance #return the updated self.balance

    # ----------------------Function---------------------------------------- #
        
    def withdrawl(self, withdraw_amt): #Method will remove funds from balance based on withdraw_amt
        self.withdraw_amt = withdraw_amt #Setting up the variable withdraw_amt
        new_amt = self.balance - withdraw_amt # Subtracting withdrawl amount from balance and storing it in new_amt
        self.balance = new_amt # dumping value from new_amt into self.balance
        return self.balance #return the updated self.balance

    # ----------------------Function---------------------------------------- #

    def display(self): # Method will give the user a readable version of their account information
        return(f"{self.name}, your account number is: {self.account} and your balance is: ${self.balance}") 


# ----------------------User-Data-Collect------------------------------- #
        
usr1 = Bank_account(100123, "John D", 50000 ) #Instantiation of usr1's account details
usr2 = Bank_account(100124, "Monkey Man", 150000 ) #Instantiation of usr2's account details

# ----------------------Processing-------------------------------------- #

usr1.deposit(25) #usr2 is asking to deposit 25 into his account
usr1.withdrawl(100) #usr1 is asking to withdraw 100 from his account
usr2.deposit(5000) #usr2 is asking to deposit 5000 into his account
usr2.withdrawl(50000) #usr2 is asking to withdraw 50,000 from his account


# ----------------------Final-Result------------------------------------ #

print()#space for readability
print(usr1.display()) #calls display function, inserting usr1's information into it.
print() #space for readability
print(usr2.display()) #calls display function, inserting usr2's information into it. 