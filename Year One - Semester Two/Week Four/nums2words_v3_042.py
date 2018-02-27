import sys

file = sys.argv[1]
mapping = {}

with open(file, 'r') as mappings:
    for line1 in mappings.readlines():
        tokens1 = line1.strip().split()
        mapping[tokens1[0]] = tokens1[1]

numbers = {'0': 'zero',
           '1': 'one',
           '2': 'two',
           '3': 'three',
           '4': 'four',
           '5': 'five',
           '6': 'six',
           '7': 'seven',
           '8': 'eight',
           '9': 'nine',
           '10': 'ten'}

for line in sys.stdin:
    new1 = []
    new2 = []
    tokens = line.strip().split()
    for token in tokens:
        try:
            new1.append(numbers[token])

        except KeyError:
            new1.append('unknown')

    for n in new1:
        try:
            new2.append(mapping[n])

        except KeyError:
            new2.append('unknown')

    new_line = ' '.join(new2)
    print(new_line)
