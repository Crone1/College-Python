import sys

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
    new = []
    tokens = line.strip().split()
    for token in tokens:
        new.append(numbers[token])
    new_line = ' '.join(new)
    print(new_line)
