from unicodedata import name


class Bank_account:
    def __init__(self, name, account_num, balance):
        self.name = name
        self.account_num = account_num
        self.balance = balance

    def display(self):
        return """
        Account Hoder:  {}
        Account NUmber: {}
        Balance:        ${}
        """.format(self.name, self.account_num, self.balance)
    
    def deposit(self, number):
        self.balance += number
    
    def withdrawl(self, number):
        self.balance -= number






david = Bank_account('David H', '0123456789', 0)

while True:
    menu = input(
        '''
        Please select a menu function

        1. View account info
        2. deposit money
        3. Withdrawl Money
        '''
    )

    if menu == "1":
        print(david.display())
    elif menu == '2':
        money = int(input('How much money would you like to add: '))
        david.balance += money
    elif menu == '3':
        money = int(input('How much money would you like to withdrawl: '))
        if money > david.balance:
            print("\nSorry you're too broke for that\n")
        else:
            david.balance -= money
        

    