#! /usr /bin/env python

import sys
s = sys.argv[1]

i = 0
while i < len(s) and not s[i].isdigit():
   i = i + 1

j = i + 1
while j < len(s) and s[j].isdigit():
   j = j + 1

if i < len(s) and j < len(s)+1:
   print s[i:j],i
