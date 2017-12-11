#! /usr /bin/env python

total = 0
i = 0
while i < len(a):
   if a[i]:
      j = str(a[i])
      if j[:len(s)] == s:
         print a[i]
   i = i + 1

