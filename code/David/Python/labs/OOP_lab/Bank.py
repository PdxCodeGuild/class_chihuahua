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
        print(f"\nYou have successfully deposited ${number}\n")
    
    def withdrawl(self, number):
        if number > self.balance:
            print(f"\nSorry ${number} is greater than your balance. Your current balance is: ${self.balance}\n")
        else:
            self.balance -= number
            print(f'\nYou have successfuly withdrawn ${number} from your account. Your current balance is: ${self.balance}\n')






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
        david.deposit(money)
    elif menu == '3':
        money = int(input('How much money would you like to withdrawl: '))
        david.withdrawl(money)


    