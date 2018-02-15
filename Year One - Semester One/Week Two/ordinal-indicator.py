#!usr/bin/env python

n=input()

if n==11 or n==12 or n==13 or n%100==11 or n%100==12 or n%100==13:
   print 'th'

elif n%10==1:
   print 'st'

elif n%10==2:
   print 'nd'

elif n%10==3:
   print 'rd'

else:
   print 'th'

