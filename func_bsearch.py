#!usr/bin/env python

def bsearch(a,q):
   low = 0
   high = len(a)
   
   while high != low:

      mid = (low + high) / 2

      if a[mid] < q:
         low = mid + 1

      else:
         high = mid
 
   return low