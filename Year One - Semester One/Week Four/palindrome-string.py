
s=raw_input()

i=0
while i<len(s)/2 and s[i]==s[len(s)-i-1]:
   i=i+1

if s[i]==s[len(s)-i-1]:
   print s

   
