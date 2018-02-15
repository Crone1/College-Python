#! /usr /bin/env python

a = []
s = raw_input()
while s != 'end':
   i = 0
   while i < len(a) and a[i] != s:
      i = i + 1
   if i == len(a):
      a.append(s)
   if i < len(a):
      
   s = raw_input()
