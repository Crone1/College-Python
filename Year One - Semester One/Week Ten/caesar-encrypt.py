
#!usr/bin/env python
import sys
s = sys.stdin.read()

a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'

i = 0
while i < s:
   j = 0 
   while j < len(a):
      if s[i] == a[j]:
         sys.stdout.write(b[j])
      else:
         sys.stdout.write(s[i])
      j = j + 1
   i = i + 1


