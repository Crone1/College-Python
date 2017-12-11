#! /usr /bin/env python

import sys
s = sys.argv[1]

j = 1
while j < len(s) and (s[j-1] != s[j]):
   j = j + 1

if j < len(s):
   print s[j-1:j+1]
