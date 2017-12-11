
#!usr/bin/env python

import sys
sex = {}

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
      if girlnames[i] in sex.keys():
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