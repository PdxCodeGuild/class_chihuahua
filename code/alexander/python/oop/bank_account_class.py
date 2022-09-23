class bank_account:
    def __init__(self, account_number, name, balance):
        self.account_number = 0####what makes this number ready
        self.name = name
        self.balance = 0####what makes this ready to receive numbers
    def deposit(self, amount):
        self.balance += amount
        print(f'current balance is {self.balance}')
    def withdrawal(self, amount):
        if amount > self.balance:
            print('not enough money to cover this transaction')
        else:
            self.balance -= amount
        print(f'remaining balance is {self.balance}')
    def bankfees(self):
        self.balance -= (self.balance * .05)
        print(f'your new balance is {self.balance}')
    def display(self):
        print(self.name)
        print(self.account_number)
        print(self.balance)
lex = bank_account(1234567, 'lex', 100)
lex.deposit(10000)
lex.display()