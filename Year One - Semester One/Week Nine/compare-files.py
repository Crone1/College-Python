
import sys

line_no = 1
s = sys.argv[1]
t = sys.argv[2]

with open(s,'r') as file_one:
   f1 = file_one.read()
   with open(t,'r') as file_two:
      f2 = file_two.read()
      i = 0
      while i < len(f2) and i < len(f1) and f1[i] == f2[i]:
         i = i + 1

#next step = find 'line_no'
      
      if i < len(f2) and i < len(f1):
         m = 0
         n = m
         while m < i:
            n = n + 1
            while n < i and f1[n] != '\n':
               i = i + 1

            if n < i:
               line_no = line_no + 1

            m = n

      print line_no, i
