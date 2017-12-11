#!usr/bin/env python

import sys

total = 0
i = 1
while i < len(sys.argv):
   total = total + int(sys.argv[i])
   i = i + 1

print total