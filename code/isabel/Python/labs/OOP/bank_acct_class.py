class Bank_account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawl(self, amount):
        if amount > self.balance:
            print('can not withdrawl')
        else:
            self.balance -= amount
            return self.balance

    def display(self):
        return f"Hello {self.name} your account number is: {self.account_number} and balance is: {self.balance}"


acct1 = Bank_account(8675309, 'golden', 0)
print(acct1.display())