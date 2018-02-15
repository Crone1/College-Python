
prev=input()


while prev!=0:
   curr=input()
   if curr>prev:
      print 'higher'
   elif prev==curr:
      print 'equal'
   elif curr!=0 and curr<prev:
      print 'lower'
   prev=curr

