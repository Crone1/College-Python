
#!/usr/bin/env python

import sys

s = sys.stdin.readlines()
a = {}

i = 0
while i < len(s):
   file = s[i].strip()
   splitfile = file.split('.')
   filename = '.'.join(splitfile[0:2])
   a[filename] = splitfile[2]

   i = i + 1

for filename in a:
   if a[filename] == 'correct':
      print filename
