#! /usr /bin/env python

import sys
largest = sys.argv[1]
i = 2
while i < len(sys.argv):
   new = int(sys.argv[i])
   if new > largest:
         largest = new
   i = i + 1

print largest
