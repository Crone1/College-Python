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
           '10': 'ten',
           '11': 'eleven',
           '12': 'twelve',
           '13': 'thirteen',
           '14': 'fourteen',
           '15': 'fifteen',
           '16': 'sixteen',
           '17': 'seventeen',
           '18': 'eighteen',
           '19': 'nineteen',
           '20': 'twenty',
           '30': 'thirty',
           '40': 'forty',
           '50': 'fifty',
           '60': 'sixty',
           '70': 'seventy',
           '80': 'eighty',
           '90': 'ninety',
           '100':'one hundred'}

for line in sys.stdin:
    new1 = []
    tokens = line.strip().split()
    for token in tokens:
        try:
            new1.append(numbers[token])

        except KeyError:
            new1.append('{}-{}'.format(numbers[str(int(token)//10) + '0'], numbers[str(int(token)%10)]))

    new_line = ' '.join(new1)
    print(new_line)
