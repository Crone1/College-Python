#! /usr /bin/env python

import sys
n = sys.argv[1]
s = sys.argv[2]

i = 0
while i < len(s):
   while i < len(s) and not s[i].isalpha():
      i = i + 1

   if s[i:i+n].isalpha():
      print s
      print i
   i = i + 1




