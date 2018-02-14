import sys

def contains(s, f):
	for c in s:
		if c in f:
			f = f.replace(c,'',1)
		else:
			return False
	return True

def main():
	for line in sys.stdin:
		line = line.strip().upper().split()
		[first,second] = line
		print(contains(first,second))			

if __name__ == '__main__':
	main()