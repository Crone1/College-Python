
a = []

s = raw_input()
while s != 'end':
   a.append(s)
   s = raw_input()

i = 0
while i < len(a):

   j = 0
   while j < len(a[i]) and a[i][j] == '0':
      j = j + 1

   if j < len(a[i]):
      a[i] = a[i][j:]

   if a[i] == '0' * len(a[i]):
      a[i] = 0

   i = i + 1

l = 0
while l < len(a):
   print a[l]
   l = l + 1
