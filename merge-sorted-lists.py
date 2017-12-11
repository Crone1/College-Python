a = []

s = raw_input()
while s != 'end':
	a.append(int(s))
	s = raw_input()

b = []

m = raw_input()
while m != 'end':
	b.append(int(m))
	m = raw_input()
	
c = []
x = 0
z = 0
while x < len(a) and z < len(b):
   if a[x] < b[z]:
      c.append(a[x])
      x = x + 1

   elif b[z] < a[x]:
      c.append(b[z])
      z = z + 1

   elif b[z] == a[x]:
       c.append(a[x])
       c.append(b[z])
       x = x + 1
       z = z + 1

if x < len(a) and not z < len(b):
   c = c + a[x:]

if not x < len(a) and z < len(b):
   c = c + b[z:]

w = 0
while w < len(c):
   print c[w]
   w = w + 1