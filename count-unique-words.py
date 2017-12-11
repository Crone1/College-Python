
import sys

a = sys.stdin.read().split()
words = {}

i = 0
while i < len(a):
   if a[i] in words:
      words[a[i]] = 'repeat'

   else:
      words[a[i]] = 'first'

   i = i + 1

for key in words: 
    if words[key] == 'first':
       sys.stdout.write(key + '\n')