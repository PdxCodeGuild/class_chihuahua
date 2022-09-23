
# Jimi Spier
# bank_account_class.py
# 20220922


class Bank_account:
    def __init__(self, account_number, name, balance):
        self.account = account_number
        self.name = name
        self.balance = balance
        
    def deposit(self, deposit_amt):
        self.deposit_amt = deposit_amt
        new_amt = deposit_amt + self.balance
        self.balance = new_amt
        return self.balance
        
    def withdrawl(self, withdraw_amt):
        self.withdraw_amt = withdraw_amt
        new_amt = self.balance - withdraw_amt
        self.balance = new_amt
        return self.balance

    def display(self):
        return(f"{self.name}, your account number is: {self.account} and your balance is: ${self.balance}")
        
usr1 = Bank_account(100123, "John D", 50000 )
usr2 = Bank_account(100124, "Monkey Man", 150000 )

usr1.deposit(25)
usr1.withdrawl(100)
usr2.deposit(5000)
usr2.withdrawl(50000)
print()
print(usr1.display())
print()
print(usr2.display())