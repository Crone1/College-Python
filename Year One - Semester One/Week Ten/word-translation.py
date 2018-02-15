
#!/usr/bin/env python

import sys
d ={}
with open('translation.txt', 'r') as trans:
   lines = trans.read().split('\n')

   m = 0
   while m < len(lines) - 1:
      split_lines = lines[m].split()
      d[split_lines[0]] = split_lines[1]
      m = m + 1

s = sys.stdin.read().split('\n')

i = 0
while i < len(s):
   if s[i] in d:
      print d[s[i]]
   i = i + 1
