
import sys

s = sys.stdin.read()
s = s.split('\n')
s = ' '.join(s)

j = 0
while j < len(s):

   i = j
   while i < len(s) and s[i] != '.' and s[i] != '!' and s[i] != '?':
      i = i + 1


   if i < len(s):
      m = s[j:i + 1].strip().capitalize()

   n = 0
   while n < len(m) and m[n:n + 4] != 'mary':
      n = n + 1

   if n < len(m):
      c = m[:n] + 'Mary' + m[n + 4:]
      print c

   elif i + 1 < len(s):
      print m

   j = i + 1