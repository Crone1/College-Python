import sys
from collections import namedtuple

Student = namedtuple('Student', ['firstname', 'surname', 'id'])


def show_student(s):
    print('First name: {}'.format(s.firstname))
    print('{:>{}s}: {}'.format('Surname', len('first name'), s.surname))
    print('{:>{}s}: {}'.format('ID', len('first name'), s.id))
