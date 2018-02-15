#! /usr /bin/env python

import sys
f = sys.argv[1]

i = 0
while i < len(f) and f[i].isdigit():
   i = i + 1

print f[:i]
print f[i+1:]
