#! /usr /bin/env python

import sys
s = sys.argv[1]

i = 0
while i < len(s) and not s[i].isupper():
   i = i + 1

if i < len(s) and s[i].isupper():
   print s[i],i
