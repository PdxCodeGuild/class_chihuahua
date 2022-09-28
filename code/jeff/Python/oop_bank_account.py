#def class_names(cls, names):
class Bank_account:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number

    #customer statement
    def cust_balance(self):
        return(f"Hi {self.name} your balance is {self.balance}")

    #deposit
    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return self.balance


    #withdraw
    def withdraw(self, withdraw):
        self.balance = self.balance - withdraw
        return self.balance


c1 = Bank_account("Jeff", 19575, "3546-123")
c2 = Bank_account("John", 12090, "4392-989")
c3 = Bank_account("Emily", 49500, "9038-344")
c4 = Bank_account("Chloe", 27, "4234-432")


print(c1.cust_balance())
    

#Bank Account Class
#Create a Python class called Bank_account which represents a bank account, having as attributes: account_number (numeric type), name (name of the account owner as string type), balance.
#Create a constructor with parameters: account_number, name, balance.
#Create a deposit() method which manages the deposit actions.
#Create a withdrawal() method which manages withdrawals actions.
#Create a display() method to display account details.