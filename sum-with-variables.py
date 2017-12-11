
import sys

s = sys.stdin.readlines()
total = 0

def integer(a):
   return a.isdigit() or (a[1:].isdigit and a[0] == '-')

def assignment_statement(a):
   i = 0
   while i < len(a) and a[i] != '=':
      i = i + 1

   return i < len(a)

numbers = {}

i = 0
while i < len(s):

   if integer(s[i].strip()):
      total = total + int(s[i].strip())

   elif assignment_statement(s[i].strip()):
      j = 0
      while j < len(s[i]) and s[i][j] != '=':
         j = j + 1

      numbers[s[i][:j].strip()] = s[i][j + 1:-1].strip()

   elif s[i].strip().isalpha():
      total = total + int(numbers[s[i].strip()])

   i = i + 1

print total