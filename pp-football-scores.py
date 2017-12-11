#! /usr /bin/env python

import sys
score = sys.argv[1]

i = 0
while i < (int(score) / 3) + 1:
   print i, int(score) - (3 * i)
   i = i + 1
