#Banking operations

class BankAccount:
    def __init__(self, account_balance):


        self.account_balance = account_balance

    def deposit(self, amount):
        self.amount = amount
        #self.amount = input()
        self.account_balance == 0
        return self.account_balance + self.amount

    def withdraw(self, amount):
        self.amount = amount
        if self.account_balance >  self.amount:
            True
            #return "Insufficient funds."
            return self.account_balance - self.amount
        else:
            False
    def display_balance(amount):
        #self.amount = amount
        #amount = input()
        print (f"Current Balance: {amount}")
