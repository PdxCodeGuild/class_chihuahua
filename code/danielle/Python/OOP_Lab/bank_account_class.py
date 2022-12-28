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
<<<<<<< HEAD

display = Bank_Account("XXX-XX-3289", "Danielle C.", 345)

display.display()


# Create a Python class called Bank_account which represents a bank account, having as attributes: account_number (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: account_number, name, balance.
# Create a deposit() method which manages the deposit actions.
# Create a withdrawal() method which manages withdrawals actions.
# Create a display() method to display account details.
=======

display = Bank_Account("XXX-XX-3289", "Danielle C.", 345)

display.display()
>>>>>>> 28a5ab8527a406c2de2ec6719bb2230bfeed4894
