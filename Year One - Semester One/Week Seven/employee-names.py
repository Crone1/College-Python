a = []
b = []

s = raw_input()
while s != 'end':
   a.append(s[:8])
   b.append(s[9:])
   s = raw_input()

j = raw_input()
while j != 'end':
   i = 0
   while i < len(a) and j != a[i]:
      i = i + 1
   if i < len(a):
      print b[i]
   j = raw_input()



