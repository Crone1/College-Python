a = []

s = raw_input()
while s != 'end':
   s = s[6:8] + '/' + s[3:5] + '/' + s[0:2] + s[8:]
   a.append(s)
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

g = 0
while g < len(a):
   print a[g][9:]
   g = g + 1