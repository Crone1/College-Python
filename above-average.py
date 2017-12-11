a =[]

s = raw_input()
while s != 'end':
	a.append(int(s))
	s = raw_input()

total = 0

i = 0
while i < len(a):
	total = total + a[i]
	i = i + 1

j = 0
while j < len(a):
	if a[j] > (total/len(a)):
		print a[j]
	j = j + 1