import sys

with open(sys.argv[1], 'r') as students:
   with open(sys.argv[2], 'r') as delinquents:
       students = set(students.readlines())
       delinquents = set(delinquents.readlines())
       matches = sorted(list(students.intersection(delinquents)))
i = 1
for match in matches:
    print('{}. {}'.format(i, match), end='')
    i += 1