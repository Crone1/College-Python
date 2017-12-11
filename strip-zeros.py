#!usr/bin/env python

import sys

a = []

s = sys.stdin.readlines()

i = 0
while i < len(s):
   s[i] = s[i].lstrip('0')
   i = i + 1

j = 0
while j < len(s):
   if s[j] == '\n':
      s[j] = '0' + '\n'
   sys.stdout.write(s[j])
   j = j + 1