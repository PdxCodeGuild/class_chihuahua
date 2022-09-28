class Bank_account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds available")
        else:
            self.balance -= amount
        
            return self.balance

    def display(self):
        return self.account_number, self.name, self.balance


jordan_account = Bank_account(1234567, "Jordan", 1000)

print(jordan_account.deposit(500))
print(jordan_account.deposit(200))
print(jordan_account.display())
#testing git