
a = []

s = raw_input()
while s != 'end':
	a.append(int(s))
	s = raw_input()

j = 0
while j < len(a):
   i = j + 1
   smallest = j
   while i < len(a):
      if a[i] < a[smallest]:
         smallest = i
      i = i + 1

   temp = a[smallest]
   a[smallest] = a[j]
   a[j] = temp

   j = j  + 1

l = 0
while l < len(a):
	print a[l]
	l = l + 1
