class Bank_Account: 
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdrawl(self, amount):
        if amount > self.balance:
            print("Insufficient funds...")
    def display(self):
        print(f"Details for account {self.account_number}, {self.name}: Your current balance is {self.balance}")

display = Bank_Account("XXX-XX-3289", "Danielle C.", 345)

display.display()
