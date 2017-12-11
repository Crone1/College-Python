
import sys
s = sys.argv[1]
i = 2
with open(s,'w') as h:
   while i < len(sys.argv):
      h.write(sys.argv[i] + '\n')
      i = i + 1
