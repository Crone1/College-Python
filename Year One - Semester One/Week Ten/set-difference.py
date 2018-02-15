import sys

c = []

with open('a.txt','r') as file_one:
   a = file_one.read().split()
   with open('b.txt','r') as file_two:
      b = file_two.read().split()
      
      if a and b:
         i = 0
         j = i
         while i < len(a) and j < len(b):
            while j < len(b) and a[i] != b[j]:
               j = j + 1

            if j == len(b):
               c.append(a[i])
            i = i + 1
            j = 0
      else:
         c = a
      m = 0
      while m < len(c):
         sys.stdout.write(c[m] + '\n')
         m = m + 1
