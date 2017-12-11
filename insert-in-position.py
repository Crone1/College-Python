a = []
s = raw_input()
while s != 'end':
   a.append(s)
   s = raw_input()

s = raw_input()

i = 0
while i < len(a) and int(s) > int(a[i]):
	i = i + 1

if i <= len(a):
   # s goes in before this number
   a.insert(i, s)

j = 0 
while j < len(a):
	print a[j]
	j = j  + 1