#! usr/bin/env python

a = []

s = raw_input()
while s != 'end':
   a.append(int(s))
   s = raw_input()

j = 0
while j < len(a):
   smallest = j
   i = j + 1
   while i < len(a):
      if a[i] < a[smallest]:
         smallest = i
      i = i + 1

   temp = a[j]
   a[j] = a[smallest]
   a[smallest] = temp

   j = j + 1

b = []

t = raw_input()
while t != 'end':
   a.append(int(t))
   t = raw_input()

m = 0
while j < len(a):
   smallest = m
   g = m + 1
   while g < len(a):
      if a[g] < a[small]:
         small = m
      g = g + 1

   temporary = a[m]
   a[m] = a[small]
   a[small] = temporary

   m = m + 1
c = []
x = 0
z = 0
while x < len(a) and z < len(b):
   if a[x] > b[z]:
      c.append(b[z])
      c.append(a[x])

   elif b[z] > a[x]:
      c.append(a[x])
      c.append(b[z])

   x = x + 1
   z = z + 1

if x < len(a) and not z < len(b):
   c.append(a[x:])

if not x < len(a) and z < len(b):
   c.append(b[z:])

w = 0
while w < len(c):
   print c[w]
   w = w + 1