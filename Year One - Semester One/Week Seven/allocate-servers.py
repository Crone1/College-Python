
a = []

s = raw_input()
while s != 'end':
   a.append(s)
   s = raw_input()

if len(a) > 0:
   server_no = 1
   most_amount = 1
else:
   server_no = 0
   most_amount = 0
i = 1
m = 0
while m < len(a):
   while i < len(a) and int(a[i]) - int(a[i-1]) > 1000:
      i = i + 1

   if i < len(a):
      j = 0
      while j + i < len(a) and int(a[i+j]) - int(a[i-1]) < 1000:
         server_no = server_no + 1
         j = j + 1
   if server_no > most_amount:
      most_amount = server_no
   server_no = 1
   i = i + j
   m = i + j 

print most_amount
