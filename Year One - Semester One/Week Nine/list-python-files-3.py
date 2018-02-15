

import os
files = os.listdir('.')
j = 0
i = 0
while i < len(files):
   if files[i][0] != '.' and files[i][len(files[i])-3:] == '.py':
      with open(files[i], 'r') as f:
         if f.read():
            j = j + 1
            while j < len(f.read(i)) and f.read(i)[j] != '\n':
               j +=1
            if i < len(f.read(i)):
               if strip(f.read(i)[:j])== '#/usr/bin/env python':
                  print files[i]
   i = i + 1
