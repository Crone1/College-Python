#! /usr /bin/env python

import sys
c = sys.argv[1]
s = raw_input()

i = 0
while i < len(s) and s[i] != c:
   i = i + 1

if i < len(s):
   print i

