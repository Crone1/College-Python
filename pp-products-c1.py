#! /usr /bin/env python

import sys
digits = sys.argv[1]
product = int(digits[0])
print product

i = 1
while i < len(digits):   
   product = product * int(digits[i])
   print product
   i = i + 1
