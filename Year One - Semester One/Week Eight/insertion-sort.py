
a = []
b = []

s = raw_input()
while s != end:

   if not s.isdigit():
      while s != 'end':
         b.append(s)
         s = raw_input()

   if s.isdigit():
      while s != 'end':
         b.append(int(s))
         s = raw_input()

i = 1
while i < len(a):
   temp = a[i]

   j = i
   while j > 0 and a[j - 1] > temp:
      a[j] = a[j - 1]
      j = j - 1

   a[j] = temp
   i = i + 1

m = 0
while m < len(a):
   print a[m]
   m = m + 1
