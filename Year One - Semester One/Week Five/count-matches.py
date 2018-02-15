#! /usr /bin/env python

import sys
pattern = sys.argv[1]
total = 0
s = raw_input()

while s != 'end':
   i = 0
   while i < len (s):
      while i < len (s) and s[i:i + len(pattern)] != pattern:
         i = i + 1
      if s[i:i + len(pattern)] == pattern:
         total = total + 1
         i = i + len(pattern)
 
   if i >= len(s):
      print total
   
   s = raw_input()
   total = 0
