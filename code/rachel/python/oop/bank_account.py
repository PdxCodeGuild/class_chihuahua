'''
Create a Python class called Bank_account which represents a bank account, having as attributes: account_number (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: account_number, name, balance.
Create a deposit() method which manages the deposit actions.
Create a withdrawal() method which manages withdrawals actions.
Create a display() method to display account details.
'''
# Create a class 'Bank_account'
class Bank_account:

    # define attributes for the 'Bank_account': account number, name, and balance
    def __init__(self, account_number, name, balance):
        self.account_number = int(account_number)
        self.name = str(name)
        self.balance = float(balance)
    
    # create new method 'deposit' which adds money to the account and returns the amount added and the new balance
    def deposit(self, dep_amount):
        self.balance += float(dep_amount)
        return f"Deposit: {dep_amount} New Balance: {self.balance}"

    # create new method 'withdrawal' which subtracts money from the account and returns the amount withdrawn and the new balance. If the attempted withdrawal exceeds available balance, will display 'insufficient funds'.
    def withdrawal(self, withdrawal_amount):
        if self.balance > withdrawal_amount:
            self.balance -= (withdrawal_amount)
            return f"Withdrawal: {withdrawal_amount} New Balance: {self.balance}"
        else:
            return f"Insufficient funds. Attemped withdrawal: {withdrawal_amount} exceeds available balance: {self.balance}"

    # create new methd 'account_details' that displays account holder name, account number, and balance.
    def account_details(self):
        self.detail = f"Name: {self.name}  Acct No: {self.account_number}  Balance: {self.balance}"
        return self.detail

# create instances of the class Bank_account with account numbers, names, and balances. 
account_1 = Bank_account(123456, "Jane Doe", 10000)
account_2 = Bank_account(123457, "Johnny Appleseed", 500)

# use print and the account_details method to display the name, account number, and balance for account_1
print(account_1.account_details())
# use print and the withdrawal method to withdraw money from account_1 and display the new balance.
print(account_1.withdrawal(15000))

# use print and the account_details method to display the name, account number, and balance for account_2
print(account_2.account_details())
# use print and the deposit method to deposit money into account_2 and display the new balance
print(account_2.deposit(1000))

