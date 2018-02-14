import sys

def main():

   s = int(sys.argv[1]) *2 -1

   i = 0
   while i < s//2 + 1:
      print ((((s//2) - i) * ' ') + ('* ' * (i)) + ('*'))
      i = i + 1

   i = i - 2
   while i > -1:
      print ((((s//2) - i) * ' ') + ('* ' * (i)) + ('*'))
      i = i - 1

if __name__ == '__main__':
	main()