a = []
b = []
c = []

s = raw_input()
while s != 'end':

   i = 0
   while i < len(s) and s[i] != ',':
      i = i + 1
   if i < len(s):
      a.append(s[:i])

      l = i + 1
      while l < len(s) and s[l] != ',':
         l = l + 1
      if l < len(s):
         b.append(s[i + 1:l])

         m = l + 1
         while m < len(s):
             m = m + 1
         c.append(s[l + 1:m])

   s = raw_input()

s = input()

if s == 0:
	x = a

if s == 1:
	x = b

if s == 2:
	x = c

j = 0
while j < len(x):
	print x[j]
	j = j + 1
