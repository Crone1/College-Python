
#!/usr/bin/env python

import sys

s = sys.stdin.readlines()
user = {}
file_status = {}

i = 0
while i < len(s):
   s[i] = s[i].strip()
   name_and_file = s[i].split('/')
   file_name_and_status = name_and_file[1].split('.')
   status = file_name_and_status[2]
   filename = '.'.join(file_name_and_status[0:2])
   file_status[filename] = status
   i = i + 1

j = 0
while j < len(s):
   s[j] = s[j].strip()
   Name_and_file = s[j].split('/')
   Name = str(Name_and_file[0])

   if Name not in user:
      user[Name] = 0

   File_name_and_status = ('/'.join(Name_and_file)).split('.')
   Filename = '.'.join(File_name_and_status[0:2])

   for Filename in file_status:
      if file_status[Filename] == 'correct':
         user[Name] = 1

   j = j + 1

for Name in user:
   print Name, user[Name]
