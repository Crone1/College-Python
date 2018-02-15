neg=0
pos=0
i=0
while i<5:
   n=input()
   if n<0:
      neg=neg+n
   else:
      pos=pos+n
   i=i+1
print neg,pos
