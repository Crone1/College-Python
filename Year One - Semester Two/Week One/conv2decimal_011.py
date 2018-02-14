import sys

def convert(first, second):
	return int(first, base=int(second))

def main():
	for line in sys.stdin:
		line = line.strip().split()
		[first,second] = line
		print(convert(first,second))			

if __name__ == '__main__':
	main()