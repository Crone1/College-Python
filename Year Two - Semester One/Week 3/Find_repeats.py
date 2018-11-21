
print('Enter numbers (-1 to end): ',end = '')
n = input().strip()
all = []
repeats = []
while n != '-1' and n:
    if n in all:
        repeats.append(n)
    all.append(n)
    n = input().strip()
    
for n in repeats:
    print(str(n) + ' ', end='')
print()