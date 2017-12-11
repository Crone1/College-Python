
import sys

total = 0
j = 1
while j < len(sys.argv):

   s = sys.argv[j]

   with open(s,'r') as s:
      f = s.readlines()
      i = 0
      while i < len(f):
         a = f[i].split()
         l = 0
         while l < len(a):
            total = total + int(a[l].strip())
            l = l + 1
         i = i + 1
   j = j + 1
sys.stdout.write(str(total) + '\n')
