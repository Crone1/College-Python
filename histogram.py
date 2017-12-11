#!/usr/bin/env python

a = [[], [], [], [], [], [], [], [], [], []]

s = raw_input()
while s != 'end':
   s = int(s)
   a[s].append(s)
   s = raw_input()

i = 0
while i < len(a):
	print i, '*' * len(a[i])
	i = i + 1