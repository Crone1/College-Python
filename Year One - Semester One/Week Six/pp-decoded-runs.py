#! /usr /bin/env python

s = raw_input()
j = ''

while s != 'END':
   j = j + s[0] * int(s[2:])
   s = raw_input()

print j
