#! usr/bin/env python

n = input()

while n != 1:
   print n
   if n % 2 == 0:
      n = n / 2
   elif n % 2 == 1:
      n = (n * 3) + 1
print n