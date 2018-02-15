
import sys

s = sys.stdin.read()
s = s.split('\n')

p = 0
while p < len(s):
   if s[p] == '':
      s[p] = '@'
   p = p + 1

s = ' '.join(s)

j = 0
while j < len(s):

   i = j
   while i < len(s) and s[i] != '.' and s[i] != '!' and s[i] != '?' and s[i] != '@':
      i = i + 1

   if i < len(s) and s[i] != '@': 
      m = s[j:i + 1].strip().capitalize()

      n = 0
      while n < len(m) and m[n:n + 4] != 'mary':
         n = n + 1

      if n < len(m):
         c = m[:n] + 'Mary' + m[n + 4:]
         print c

      elif i < len(s):
         sys.stdout.write(m)
         if i + 24 < len(s):
            sys.stdout.write('\n')

   elif i < len(s) and s[i] == '@':
      sys.stdout.write('\n')

   j = i + 1
