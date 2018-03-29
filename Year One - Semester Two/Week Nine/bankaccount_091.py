
class BankAccount(object):

    account_type = 'General'
    next_account_number = 16555232
    overdraft = 0

    def __init__(self, forename, surname, balance):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number

        BankAccount.next_account_number += 1

    def lodge(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount

        else:
            print('Insufficient funds available')

    def __str__(self):
        l = []
        l.append('Name: {}'.format(self.forename + ' ' + self.surname))
        l.append('Account number: {}'.format(self.account_number))
        l.append('Account type: {}'.format(self.account_type))
        l.append('Balance: {:.02f}'.format(self.balance))
        return '\n'.join(l)


class CurrentAccount(BankAccount):

    account_type = 'Current'
    overdraft = -1000

    def withdraw(self, amount):
        if self.balance > -1000:
            self.balance = self.balance - amount

        if self.balance <= -1000:
            print('Insufficient funds available')

    def __str__(self):
        l = []
        if self.balance < 0:
        	self.balance += 1000
        l.append(super().__str__())
        l.append('Overdraft: {:.02f}'.format(self.overdraft))

        return '\n'.join(l)


class SavingsAccount(BankAccount):

    account_type = 'Savings'
    intrest = 0.01

    def apply_interest(self):
        self.balance = self.balance * (1 + self.intrest)

    def __str__(self):
        l = []
        l.append(super().__str__())
        l.append('Interest rate: {}'.format(self.intrest))
        return '\n'.join(l)
