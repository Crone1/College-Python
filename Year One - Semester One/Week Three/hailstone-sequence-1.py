n=input()
m=input()

i=0
while i<n:
   if i==0:
      print m
   elif i>0:
      if (m/2)*2==m:
         m=m/2
         print m
      
      else:
         m=(m*3)+1
         print m
   i=i+1
