import sys

ball_one = sys.argv[1]
ball_two = sys.argv[2]
ball_three = sys.argv[3]

matches = 0

a = sys.stdin.readlines()
j = 0
while j < len(a):

   i = 0
   while i < len(a[j]) and a[j][i] != ball_one:
        i = i + 1

   if i < len(a[j]):
        matches = matches + 1

   m = 0
   while m < len(a[j]) and a[j][m] != ball_two:
        m = m + 1

   if m < len(a[j]):
        matches = matches + 1

   n = 0
   while n < len(a[j]) and a[j][n] != ball_three:
        n = n + 1

   if n < len(a[j]):
        matches = matches + 1

   if matches == 0:
      print 0
   elif matches == 1:
         print 1

   elif matches == 2:
         print 5

   elif matches == 3:
         print 100
   j = j + 1