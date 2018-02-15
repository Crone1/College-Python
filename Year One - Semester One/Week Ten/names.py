
#!usr/bin/env python

import sys
sex = {}
with open('boys.txt', 'r') as boy:
   with open ('boys.txt', 'r') as girl:
      boynames = boy.readlines()
      girlnames = girl.readlines()
      i = 0
      while i < len (s):
         while i < len (s) and s[i:i + len(pattern)] != pattern:
            i = i + 1
         if s[i:i + len(pattern)] == pattern:
            total = total + 1
            i = i + len(pattern)

with open('boys.txt', 'r') as boy:
   boynames = boy.readlines()
   i = 0
   while i < len(boynames):
      sex[boynames[i]] = 'boy'
      i = i + 1

with open('girls.txt', 'r') as girl:
   girlnames = girl.readlines()
   i = 0
   while i < len(girlnames):
      if sex[girlnames[i]] == 'boy':
         sex[girlnames[i]] = 'either'

      else:
         sex[girlnames[i]] = 'girl'
      i = i + 1

names = sys.stdin.readlines()

i = 0
while i < len(names):
   if names[i] in sex:
      print names[i].strip() + ' ' + sex[names[i]]
   i = i + 1
