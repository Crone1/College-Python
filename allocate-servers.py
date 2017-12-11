a = []

s = raw_input()
while s != 'end':
   a.append(s)
   s = raw_input()

server_no = 0
most_amount = 0

j = 0
i = 0
while i < len(a):
   j = i
   while j < len(a) and int(a[j]) < int(a[i]) + 1000:
      server_no = server_no + 1
      j = j + 1

   if server_no > most_amount:
      most_amount = server_no
   server_no = 0

   i = i + 1

print most_amount