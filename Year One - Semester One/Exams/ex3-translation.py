
#!usr/bin/env python

import sys
import os

s = sys.stdin.readlines()                          #list of lines with newlines

with open('translation.txt', 'r') as file_name:
   contents = file_name.readlines()                         #list with newlines

translation = {}                                               #make dictionary


i = 0
while i < len(contents):
   line = contents[i].strip()
   tokens = []

   f = 0
   while line[f] != ' ':
      f = f + 1
   
   tokens.append(line[:f])

   p = f
   while p < len(line) and line[p] == ' ':   #put translations in a dictionary
      p = p + 1

   tokens.append(line[p:])

   translation[tokens[0]] = tokens[1]
   i = i + 1

j = 0
while j < len(s):
   s[j] = s[j].split(' ')                       #make list of words within list
   j = j + 1

m = 0
while m < len(s):
   while s[m] == '':
      s.pop(m)

   l = 0
   while l < len(s[m]):
      while s[m][l] == '':
         s[m].pop(l)

      if s[m][l] in translation:               #search xfor word in translation
         s[m][l] = translation[s[m][l]]

      elif s[m][l].rstrip('\n') in translation:  #search xfor word with newline
         s[m][l] = translation[s[m][l]].strip()

      l = l + 1

   m = m + 1

k = 0
while k < len(s):
   s[k] = ' '.join(s[k])                    #join each element together together
   k = k + 1

final = ''.join(s)                                           #make list a string

sys.stdout.write(final)                                            #print string
