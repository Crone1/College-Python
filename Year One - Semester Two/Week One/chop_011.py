import sys

def chop(s):
	return s[1:-1]

def main():
	for s in sys.stdin:
		line = chop(s.strip())
		if line:
			print(line)

if __name__ == '__main__':
	main()