
s=raw_input()
t=""

i=0
while i<((len(s) + 1)/2):
   t = t + s[i*2]
   i=i+1

print t
