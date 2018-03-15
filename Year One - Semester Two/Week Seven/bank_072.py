
class BankAccount(object):

    def __init__(self, balance=0.00):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, money):
        if self.balance - money >= 0:
            self.balance -= money

        else:
            print('Insufficient funds available')

    def __str__(self):
        return 'Your current balance is: {:<.2f} euro'.format(self.balance)
