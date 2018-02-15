
import os
files = os.listdir('.')

i = 0
while i < len(files):
   if files[i][0] != '.' and files[i][len(files[i])-4:] != '.bak':
      copy = files[i] + '.bak'
      with open(copy, 'w') as backup:
         with open(files[i], 'r') as file:
            text = file.read()
            backup.write(text)

   i = i + 1
