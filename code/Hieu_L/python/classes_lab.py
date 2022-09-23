import pick6
class bank_account:
    def __init__(self, name, balance, account_number)
        self.name = input('enter your name: ')
        self.balance = 0

    def __repr__(self):
        return print("account number: {self.account_number} \n name: {self.name} \n account number: {self.account_number}")

    def deposit(self):
        amount = input('enter deposit amount: ')
        self.balance += amount
        return self.balance
    
    def withdrawal(self):
        amount = input('enter withdrawal amount: ')
        self.balance -= amount
        return self.balance
