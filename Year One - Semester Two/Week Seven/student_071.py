
class Student(object):

    def __init__(self, sid, surname, forename, modlist = []):
        self.sid = sid
        self.surname = surname
        self.forename = forename
        self.modlist = modlist

    def add_module(self, module):
        self.modlist.append(module)

    def del_module(self, module):
        i = 0
        while i < len(self.modlist):
            if module == self.modlist[i]:
                self.modlist.pop(i)
            i = i + 1

    def print_details(self):
        print('ID: {}'.format(self.forename))
        print('Surname: {}'.format(self.sid))
        print('Forename: {}'.format(self.surname))
        print('Modules: {}'.format(' '.join(self.modlist)))
