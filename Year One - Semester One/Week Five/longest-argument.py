#! /usr /bin/env python

import sys
longest = ''

i = 1
while i < len(sys.argv):
   new = sys.argv[i]
   if len(new) > len(longest):
      longest = new
   i = i + 1

print longest
