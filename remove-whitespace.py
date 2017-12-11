
s=raw_input()
t=''

i=0
while i<len(s):
   if not s[i].isspace():
      t=t+s[i]
   i=i+1
print t

