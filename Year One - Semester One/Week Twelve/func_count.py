
import func_bsearch

def count(a,q):
   p = func_bsearch.bsearch(a,q)
   pp = func_bsearch.bsearch(a,q+1)
   return pp - p
