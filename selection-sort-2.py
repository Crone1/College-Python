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

   temp = a[0]
   a[0] = a[i]
   a[i] = temp

j = j + 1


