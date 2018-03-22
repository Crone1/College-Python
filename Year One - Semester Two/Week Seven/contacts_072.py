
class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__():
        return str(self.name) + ' ' + str(self.phone) + ' ' + str(self.email)


class ContactList(object):

    def __init__(self, d={}):
        self.d = d

    def add_contact(self, Contact):
        self.d[Contact.name] = Contact.phone, Contact.email

    def del_contact(self, name):
        for key in self.d:
            if key == name:
                self.d.pop(key)
                break

    def get_contact(self, name):
        try:
            return str(name) + ' ' + str(self.d[name][0]) + ' ' + str(self.d[name][1])

        except KeyError:
            return '{} : No such contact'.format(name)

    def __str__(self):
        s = ''
        for k, v in sorted(self.d.items()):
            s = s + str(k) + ' ' + str(v[0]) + ' ' + str(v[1]) + '\n'
        return 'Contact list\n------------\n{}'.format(s[:-1])
