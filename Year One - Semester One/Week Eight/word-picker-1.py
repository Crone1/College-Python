
a = []
b = []

s = raw_input()
while s != 'end':
   a.append(s)
   s = raw_input()

s = raw_input()
while s != 'end':
   b.append(int(s))
   s = raw_input()

i = 0
while i < len(b):
   print a[b[i]]
   i = i + 1
