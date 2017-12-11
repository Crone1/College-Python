a = []

i = 0
while i < 3:
	s = input()
	a.append(s)
	i = i + 1

smallest = 0
i = 1
while i < len(a):
    if a[i] < a[smallest]:
   	   smallest = i
    i = i + 1

largest = 0
m = 1
while m < len(a):
	if a[m] > a[largest]:
		largest = m
	m = m + 1

j = 0
while j < len(a) and j == smallest or j == largest:
	j = j + 1

print a[smallest]
print a[j]
print a[largest]