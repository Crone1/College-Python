
#!/usr/bin/env python

import sys

s = sys.stdin.readlines()
file_user = {}
file_status = {}
correct_files = []
user = {}

i = 0
while i < len(s):
   s[i] = s[i].strip()
   user_and_file = s[i].split('/')
   file_name_and_status = user_and_file[1].split('.')
   file = '.'.join(file_name_and_status[0:2])
   status = file_name_and_status[2]
   username = user_and_file[0]
   user_numb = username.split('-')
   numb = user_numb[1]
   user[numb] = True
   user_file = str(numb) + str(file)

   file_status[user_file] = status

   file_user[user_file] = numb

   i = i + 1

correct_per_user = (('0.' * (len(user) + 1)).split('.'))[:-1]

for (user_file) in file_status:
   if file_status[user_file] == 'correct':
      correct_files.append(user_file)

j = 0
while j < len(correct_files):
   for correct_files[j] in file_status:
      if file_status[correct_files[j]] == 'correct':
         correct_per_user[int(file_user[correct_files[j]])] = int(correct_per_user[int(file_user[correct_files[j]])]) + 1
   j = j + 1

n = 1
while n <= len(user):
   print 'user-' + str(n), (int(correct_per_user[n]) / len(correct_files))
   n = n + 1