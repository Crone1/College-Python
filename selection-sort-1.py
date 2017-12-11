a = []

s = raw_input()
while s != 'end':
   a.append(int(s))
   s = raw_input()

smallest = 0
i = 1
while i < len(a):
   if a[i] < a[smallest]:
      smallest = i
   i = i + 1

print smallest
