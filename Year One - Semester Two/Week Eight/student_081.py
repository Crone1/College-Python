
from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

DS1_MODULES = {'MS103': Module('MS103', 'Linear Mathematics 1', 5),
               'MS104': Module('MS104', 'Linear Mathematics 2', 5),
               'MS117': Module('MS117', 'Probability 1', 5),
               'MS126': Module('MS126', 'Calculus', 10),
               'CA115': Module('CA115', 'Digital Innovation Enterprise Management', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA119': Module('CA119', 'Data Science and Databases', 5),
               'CA120': Module('CA120', 'Collaboration and Innovation', 5)}


class Student(object):

    def __init__(self, idnum, surname, firstname, mods=DS1_MODULES):
        self.__idnum = idnum
        self.__surname = surname
        self.__firstname = firstname
        self.__mods = mods
        self.__marks = {code: 0 for code in self.__mods.keys()}

    def __str__(self):
        name = '{} : {} {}'.format(self.__idnum,
                                   self.__firstname,
                                   self.__surname)
        uline = '-' * len(name)
        results = '\n'.join([code + ' : ' + self.__mods[code].title +
                             ' : ' + str(self.__marks[code])
                             for code in sorted(self.__mods.keys())])
        pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            outcome = 'Pass'
        elif self.passed_by_compensation():
            outcome = 'Pass by compensation'
        else:
            outcome = 'Fail'

        return '\n'.join([name, uline, results, pm, outcome])

    def add_mark(self, mod, mark):
        self.__marks[mod] = mark

    def precision_mark(self):
        total = 0
        credits = 0
        for mod in DS1_MODULES:
            credits = credits + int(DS1_MODULES[mod][2])

            total += self.__marks[mod] * int(DS1_MODULES[mod][2])

        return total / credits

    def passed(self):
        for mark in self.__marks.values():
            if mark < 40:
                return False

        return True

    def passed_by_compensation(self):
        tot_cred = 0
        for mod in DS1_MODULES:
            tot_cred += int(DS1_MODULES[mod][2])

        tot_cred = tot_cred / 6
        for k, mark in self.__marks.items():
            if mark < 40 and mark >= 35 and self.precision_mark() >= 45 and tot_cred >= 0:
                tot_cred -= int(DS1_MODULES[k][2])
                continue

            elif mark < 40:
                return False

        if mark >= 35 and self.precision_mark() >= 45 and tot_cred >= 0:
            return True

        else:
            return False

def main():

    s1 = Student(17377463, 'Crone', 'Nathan')
    s1.add_mark('MS103', 75)
    s1.add_mark('CA116', 93)
    s1.add_mark('CA119', 80)
    s1.add_mark('CA120', 72)
    s1.add_mark('CA117', 40)
    s1.add_mark('MS117', 40)
    s1.add_mark('MS104', 40)
    s1.add_mark('CA115', 40)
    s1.add_mark('MS126', 35)

    print(s1)
                        
if __name__ == '__main__':
    main()
