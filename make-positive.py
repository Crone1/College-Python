#! /usr /bin/env python

n = raw_input()

while n != 'end':
   if n.isdigit():
      print n

   elif n[1:].isdigit():
         print n[1:]
      
   n = raw_input()
