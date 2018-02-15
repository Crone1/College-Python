#! /usr /bin/env python

import sys

s = raw_input()

while s != 'end':

   i = 0
   while i < len(s) and s[i] != '+':
      i = i + 1

   j = i + 1
   while j < len(s) and s[j] != '+':
      j = j + 1

   if j < len(s) and s[i:j] >= 4 and s[j-3:j] == '.py':
      print s[i+1:j]

   s = raw_input()
