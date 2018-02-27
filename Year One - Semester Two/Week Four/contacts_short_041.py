import sys

file = sys.argv[1]
names = {}

with open(file, 'r') as contents:
    lisht = contents.readlines()
    for line in lisht:
        names[line.strip().split()[0]] = line.strip().split()[1]

for name in sys.stdin:
        if name.strip() in names:
            print('Name: {}'.format(name.strip()))
            print('Phone: {}'.format(names[name.strip()]))

        else:
            print('Name: {}'.format(name.strip()))
            print('No such contact')
