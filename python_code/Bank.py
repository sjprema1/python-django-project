#Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions

class Bank:
    def __init__(self,):
        self.customers ={}

    def create_account(self,account_number,account_holder_name,initial_balance):
        if account_number in self.customers:
            print("the account already exists")
        else:
            self.customers['account_number'] = initial_balance
            print("the account created successfully")
            print(self.customers)

    def make_deposit(self,account_number,amount):
        if account_number in self.customers:
            self.customers['account_number'] +=amount
            print("deposit suceesfully" )

    def make_withdraw(self,account_number,amount):
        if account_number in self.customers:
            if self.customers['account_number'] >=amount:
                self.customers['account_number'] -=amount
                print("withdaw suceesfully" )

    def check_balance(self,account_number,):
        if account_number in self.customers:
            balance = self.customers['account_number']
            print(f"your account balance is {balance}")


B =Bank()
B.create_account('9876543','jhg',0)
B.make_deposit('9876543','600')
B.make_withdraw('9876543','500')
B.check_balance('9876543')




