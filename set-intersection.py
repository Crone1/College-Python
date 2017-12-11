
import sys

seen = []
c =[]

with open('a.txt','r') as file_one:
   a = file_one.read().split()
   with open('b.txt','r') as file_two:
      b = file_two.read().split()

      i = 0
      j = i
      while i < len(a) and j < len(b):
      	 j = 0
         while j < len(b) and a[i] != b[j]:
            j = j + 1

         if j < len(b):
            c.append(a[i])
         i = i + 1

      i = 0
      j = i
      while i < len(a) and j < len(b):
         i = 0
         while i < len(a) and a[i] != b[j]:
            i = i + 1

         if i < len(a):
         	c.append(b[j])
         j = j + 1

      m = 0
      while m < len(c):
         n = 0
         while n < len(seen) and c[m] != seen[n]:
            n = n + 1

         if n == len(seen):
            sys.stdout.write(c[m] + '\n')
            seen.append(c[m])
         m =  m + 1