i=0
n=input()
while i<5:
   j=input()
   if j>n:
      print 'higher'
      n=j
   elif n==j:
      print 'equal'
   else:
      print 'lower'
      n=j
   i=i+1
