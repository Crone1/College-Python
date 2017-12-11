
import sys

s = sys.argv[1]
t = sys.argv[2]

with open(s,'r') as file_one:
   f1 = file_one.readlines()

   with open(t,'r') as file_two:
      f2 = file_two.readlines()

      line = 0
      while line < len(f2) and line < len(f1) and f1[line] == f2[line]:
         line = line + 1

      position = 0
      if line < len(f2) and line < len(f1):

         while position < len(f1[line]) and position < len(f2[line]) and f1[line][position] == f2[line][position]:
            position = position + 1

         if f1[line][position] != f2[line][position] or position == len(f1[line]) or position == len(f2[line]):
            print line, position

      elif line < len(f2) or line < len(f1):
         print line, position