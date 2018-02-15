
a = []
b = []

s = raw_input()
while s != 'end':
   a.append(s)
   s = raw_input()

s = raw_input()
while s != 'end':
   b.append(s)
   s = raw_input()

line = ''
i = 0
while i < len(b): 

   while i < len(b) and b[i].isdigit():
      line = line + ' ' + a[int(b[i])]
      i = i + 1

   print line[1:]
   line = ''
   i = i + 1
