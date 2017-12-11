smallest = a[0]

i = 1
while i < len(a):

   if a[i] <= smallest:
      smallest = a[i]
   i = i + 1

j = 0
while j < len(a) and a[j] != smallest:
	j = j + 1

if j < len(a):
   print j