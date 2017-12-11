
a = []

s = raw_input()
while s != 'end':
   a.append(s)
   s = raw_input()

j = 0
while j < len(a):

   smallest = j
   i = j + 1
   while i < len(a):
	   if a[smallest] > a[i]:
	      smallest = i
	   i = i + 1

   temp = a[j]
   a[j] = a[smallest]
   a[smallest] = temp 

   j = j + 1

mode_amount = 0
mode = 0
m = 0
while m < len(a):

   x = m + 1
   while x < len(a) and a[x] == a[m]:
      x = x + 1

   if x - m > mode_amount:
      mode_amount = x - m
      mode = a[m]

   m = x

print mode,mode_amount