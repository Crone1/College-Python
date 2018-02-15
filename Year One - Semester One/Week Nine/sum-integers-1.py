
import sys

s = sys.argv[1]

lines = s
total = 0
i = 0
while i < len(lines):
   total = total + int(lines[i])
   i = i + 1

sys.stdout.write(str(total) + '\n')
