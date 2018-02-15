
a = []
s = raw_input()

while s != 'end':
   a.append(int(s))
   s = raw_input()

s = input()
i = len(a)
while i > 0 and a[i - 1] > s:
   i = i - 1

b = a[:i] + [s] + a[i:]

print b

