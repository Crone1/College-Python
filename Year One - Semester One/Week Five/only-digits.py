#! /usr /bin/env python

import sys
total = ''
s = sys.argv[1]

i = 0
while i < len(s):
   if s[i].isdigit():
      total = total + str(s[i])
   i = i + 1

print total
