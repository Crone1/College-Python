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

m = 0
while m < len(a):
   print a[m]
   m = m + 1


