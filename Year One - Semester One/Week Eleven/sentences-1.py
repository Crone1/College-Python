
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
      print s[j:i + 1].strip()

   j = i + 1
