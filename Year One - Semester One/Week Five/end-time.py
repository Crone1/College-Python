#! /usr /bin/env python

import sys
s = sys.argv[1]
n = sys.argv[2]

i = 0
while i < len(s):
   if not s[i].isdigit():
      j = i
   i = i + 1

start_time = (int(s[:j])*60 + int(s[j+1:]))

l = 0
while l < len(n):
   if not n[l].isdigit():
      k = l
   l = l + 1

duration = (int(n[:k])*60 + int(n[k+1:]))

finish_time_mins = start_time + duration

finish_time_hrs = (finish_time_mins/60)%24

finish_time_hrs_mins = str(finish_time_mins%60)

if int(finish_time_hrs_mins) < 10:
   finish_time_hrs_mins = '0' + str(finish_time_hrs_mins)

print str(finish_time_hrs) + ':' + str(finish_time_hrs_mins)
