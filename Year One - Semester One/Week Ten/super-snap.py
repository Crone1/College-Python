
#!/usr/bin/env python
import sys

d = {}

s = sys.stdin.readline().strip()
while s and s not in d:
   d[s] = True
   s = sys.stdin.readline().strip()

if s:
   print "snap:", s
   
