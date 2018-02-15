
#!/usr/bin/env python

import sys

numer = {'one': 'eins',
	 'two': 'zwei',
	 'three': 'drei',
	 'four': 'vier',
	 'five': 'funf',
	 'six': 'sechs',
	 'seven': 'sieben',
	 'eight': 'acht',
	 'nine': 'neun',
	 'ten': 'zehn'}

s = sys.stdin.read().split('\n')
i = 0
while i < len(s):
   if s[i] in numer:
      print numer[s[i]]

   i = i + 1


