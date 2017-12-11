
import sys
s = int(sys.argv[1])

i = 0
while i < s/2 + 1:
   print (((s/2) - i) * ' ') + ('*' * (i + 1)) + ('*' * i)
   i = i + 1

i = i - 2
while i > -1:
   print (((s/2) - i) * ' ') + ('*' * (i + 1)) + ('*' * i)
   i = i - 1
