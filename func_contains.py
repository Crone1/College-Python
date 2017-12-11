#!usr/bin/env python

import func_bsearch

def contains(a,q):
   p = func_bsearch.bsearch(a,q)
   return p <= len(a) - 1 and a[p] == q

def main():
   a = [2, 4, 5]
   print(bsearch(a, 4))
  print(contains(a, 3))


if __name__ == "__main__":
  main()