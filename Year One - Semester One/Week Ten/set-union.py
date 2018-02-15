
import sys

seen = []

with open('a.txt','r') as file_one:
   a = file_one.read()
   with open('b.txt','r') as file_two:
      b = file_two.read()
      c = b + a
      c = c.split()

      i = 0
      while i < len(c):
         j = 0
         while j < len(seen) and c[i] != seen[j]:
            j = j + 1

         if j == len(seen):
            sys.stdout.write(c[i] + '\n')
            seen.append(c[i])
         i = i + 1
