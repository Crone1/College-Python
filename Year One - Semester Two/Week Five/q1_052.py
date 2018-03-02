import sys

[s, n] = sys.argv[1:]

while int(n) > len(s):
    n = int(n) - len(s)

print(s[-int(n):] + s[:-int(n)])
