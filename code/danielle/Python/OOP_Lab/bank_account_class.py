
class Bank_Account: 
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Your current balance is {self.balance}")
    def withdrawl(self, amount):
        if amount > self.balance:
            print("Insufficient funds...")
    def bankFees(self):
        print(f"Current bank fees asociated with your account are {(self.balance) * .05}")
    def display():
        print(f"{Bank_Account}")

Dani_account = Bank_Account("XXX-XX-3289", "Danielle C.", 345)
Dani_account.deposit(20)
Dani_account.withdrawl(40)
Dani_account.bankFees()
Dani_account.display

print(Dani_account)