#! /usr /bin/env python

a = []
line = raw_input()
while line != 'end':
   a.append(line)
   line = raw_input()

n = input()

i = 0
while i < len(a):
   print int(a[i])+n
   i = i + 1
