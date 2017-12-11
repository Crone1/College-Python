
import sys

s = sys.argv[1]

with open(s,'r') as s:
   file = s.readlines()
   total = 0
   i = 0
   while i < len(file):
      total = total + int(file[i].strip())
      i = i + 1

sys.stdout.write(str(total) + '\n')
