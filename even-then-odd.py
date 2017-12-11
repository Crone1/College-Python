#! /usr /bin/env python

a = []
line = raw_input()
while line != 'end':
   a.append(line)
   line = raw_input()

i = 0
while i < len(a):
   while i < len(a) and int(a[i]) % 2 == 0:
      print a[i]
      i = i + 1
   i = i + 1

j = 0
while j < len(a):
   while j < len(a) and int(a[j]) % 2 == 1:
      print a[j]
      j = j + 1
   j = j + 1

