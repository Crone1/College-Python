import sys

def capitalise(s):
	return s[0].upper() + s[1:-1] + s[-1].upper()

def main():
	for line in sys.stdin:
		if len(line.strip()) > 1:
			line = capitalise(line.strip())
			print(line)
 
if __name__ == '__main__':
	main()