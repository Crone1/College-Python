import sys

s = sys.argv[1].strip()

new = ''

i = 1
while i < len(s) or i - 1 < len(s):
    if i < len(s):
        new = new + s[i] + s[i - 1]

    else:
        new = new + s[i - 1]
        
    i = i + 2

print(new)
