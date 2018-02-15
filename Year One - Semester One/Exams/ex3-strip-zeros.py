
a = []

s = raw_input()
while s != 'end':
   a.append(int(s))
   s = raw_input()

i = 0
while i < len(a):
   smallest = i
   j = i + 1
   while j < len(a):
      if a[j] < a[smallest]:
         smallest = j
      j = j + 1

   temp = a[i]
   a[i] = a[smallest]
   a[smallest] = temp

   i = i + 1

b = a[:10]

l = 0
while l < len(b):
   print b[l]
   l = l + 1
