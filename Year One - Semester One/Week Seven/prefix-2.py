#! /usr /bin/env python

i = 0
while i < len(a) and a[i][:len(s)] != s:
   i = i + 1
if i < len(a):
   print a[i]
