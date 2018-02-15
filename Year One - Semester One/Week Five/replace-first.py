#! /usr /bin/env python

import sys
pattern = sys.argv[1]
replacement = sys.argv[2]
s = raw_input()

while s != 'end':
   i = 0
   while i < len(s) and s[i:i + len(pattern)] != pattern:
      i = i + 1
   if s[i:i + len(pattern)] == pattern:
      print s[:i] + replacement + s[i + len(pattern):]
   elif i == len(s):
      print s
   s = raw_input()
