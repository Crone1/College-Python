
import func_bsearch

def sum_range(a,q,l):
   p = func_bsearch.bsearch(a,q)
   total = 0

   i = p
   while i < len(a) and a[i] < l:
      total = total + a[i]
      i = i + 1

   return total


def main():
	a = [2, 4, 4, 7, 10, 10, 11, 20, 25, 25, 25, 25, 26]
	print(sum_range(a, 1, 6))


if __name__ == "__main__":
	main()
