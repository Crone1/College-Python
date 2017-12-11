
#!usr/bin/env python

import sys

a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
cipher = {}

j = 0
while j < len(a):
	cipher[b[j]] = a[j]
	j = j + 1

s = sys.stdin.read()

i = 0
while i < len(s):
    if s[i] in cipher:
       sys.stdout.write(cipher[s[i]])

    else:
       sys.stdout.write(s[i])
    i = i + 1