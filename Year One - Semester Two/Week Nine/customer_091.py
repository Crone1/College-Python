
class Customer(object):

    discount = 0

    def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
        self.name = name
        self.balance = balance
        self.addr_line3 = addr_line3
        self.addr_line2 = addr_line2
        self.addr_line1 = addr_line1

    def owes(self):
        return self.balance * (1 - float('0.' + str(self.discount)))

    def __str__(self):
        l = []
        l.append('{}'.format(self.name))
        l.append('{}'.format(self.addr_line1))
        l.append('{}'.format(self.addr_line2))
        l.append('{}'.format(self.addr_line3))
        l.append('Balance: {:.02f}'.format(self.balance))
        l.append('Discount: {}%'.format(self.discount))
        l.append('Amount due: {:.02f}'.format(self.owes()))
        return '\n'.join(l)


class ValuedCustomer(Customer):

    discount = 10
