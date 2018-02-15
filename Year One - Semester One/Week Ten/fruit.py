
#!/usr/bin/env python

import sys

fruit = {'apple': True,
	 'pair': True,
	 'orange': True,
	 'banana': True,
	 'cherry': True}

s = sys.stdin.read().split('\n')
i = 0
while i < len(s):
   if s[i] in fruit:
      print s[i]

   i = i + 1


