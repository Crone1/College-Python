#! /usr /bin/env python

a = []
line = raw_input()
while line != 'end':
   a.append(line)
   line = raw_input()

i = 0
while i < len(a):
   print i,len(a),a[i]
   i = i + 1
