#! /usr /bin/env python
import sys
n = sys.argv[1]
j=0

i=0
while i < len(n):
   if not n[i].isdigit():
      j=i
   i = i + 1

print (int(n[:j])*60 + int(n[j+1:]))


