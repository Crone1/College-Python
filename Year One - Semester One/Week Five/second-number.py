#! /usr /bin/env python

import sys
s = sys.argv[1]

i = 0
while i < len(s) and not s[i].isdigit():
   i = i + 1

j = i + 1
while j < len(s) and s[j].isdigit():
   j = j + 1

l = j
while l < len(s) and not s[l].isdigit():
   l = l + 1

k = l + 1
while k < len(s) and s[k].isdigit():
   k = k + 1

if l < len(s) and k < len(s)+1:
   print s[l:k],l

