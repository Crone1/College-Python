#! /usr /bin/env python
a = []
line = raw_input()
while line != 'end':
   a.append(line)
   line = raw_input()

temp = ''
i = 0
while i < len(a)/2:
   temp = a[i]
   a[i] = a[len(a)-i-1]
   a[len(a)-i-1] = temp
   i = i + 1

j = 0
while j < len(a):
   print a[j]
   j = j + 1
