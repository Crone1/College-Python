
import sys

with open('irish-dobs.txt','r') as irish:
   with open('american-dobs.txt','w') as amer:

      a = irish.readlines()
      i = 0
      while i < len(a):
         s = a[i].split('/')
         temp = s[0]
         s[0] = s[1]
         s[1] = temp
         s = '/'.join(s)
         amer.write(s)
         i = i + 1
