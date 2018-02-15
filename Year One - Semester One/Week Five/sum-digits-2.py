#! /usr /bin/env python

import sys
total = 0
s = sys.argv[1]

i = 0
while i < len(s):
   if s[i].isdigit():
      total = total + int(s[i])
   i = i + 1

print total
