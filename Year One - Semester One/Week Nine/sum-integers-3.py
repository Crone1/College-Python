
import sys

total = 0
j = 1
while j < len(sys.argv):

   s = sys.argv[j]

   with open(s,'r') as s:
      file = s.readlines()
      i = 0
      while i < len(file):
         total = total + int(file[i].strip())
         i = i + 1
   j = j + 1
sys.stdout.write(str(total) + '\n')
