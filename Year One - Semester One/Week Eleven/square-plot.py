
import sys

n = int(sys.argv[3])
x = int(sys.argv[1])
y = int(sys.argv[2])

sys.stdout.write(' ' + '-' * 20 + '\n')

lines_till_next = 20 - y - n

i = 0
while i < lines_till_next:
   sys.stdout.write('|' + (' ' * 20) + '|' + '\n')
   i = i + 1

sys.stdout.write('|' + (' ' * x) + ('*' * n) + (' ' * (20 - x - n)) + '|' + '\n')

j = 0
while j < (n - 2):
   sys.stdout.write('|' + (' ' * x) + '*' + (' ' * (n - 2)) + '*' + (' ' * (20 - x - n)) + '|' + '\n')
   j = j + 1

sys.stdout.write('|' + (' ' * x) + ('*' * n) + (' ' * (20 - x - n)) + '|' + '\n')

k = 0
while k < y:
   sys.stdout.write('|' + (' ' * 20) + '|' + '\n')
   k = k + 1

sys.stdout.write(' ' + '-' * 20 + '\n')
