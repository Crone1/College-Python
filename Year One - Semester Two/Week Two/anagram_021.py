import sys

def anagram_checker(f, s):
	for c in f:
		if c in s and s:
			s = s.replace(c,'',1)

		else:
			return False

	if s:
		return False

	return True

def main():
	for line in sys.stdin:
		[first, second] = line.strip().split()
		print (anagram_checker(first, second))

if __name__ == '__main__':
	main()