#! usr/bin/env python

n = input()
total = 0

i = 0
while i < n:
   type_score = raw_input()
   if type_score == 'try':
      total = total + 5
   elif type_score == 'conversion':
      total = total + 2
   elif type_score == 'penalty':
      total = total + 3
   i = i + 1

print total