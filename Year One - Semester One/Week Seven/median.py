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

if (len(a) / 2) * 2 != len(a):
   m = (((len(a)) + 1)/2) - 1

else:
   m = len(a)/2
print a[m]

