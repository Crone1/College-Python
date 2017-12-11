import os
files = os.listdir('.')

i = 0
while i < len(files):
   if files[i][0] != '.':
      with open(files[i], 'r') as f:
            if files[i][len(files[i])-3:] == '.py' and f.read():
               print files[i]

            elif f.readline() == '#!/usr/bin/env python\n':
               print files[i]
   i = i + 1