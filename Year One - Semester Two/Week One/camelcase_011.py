import sys

def main():
	for line in sys.stdin:
		words = line.strip().split()

		i = 0
		while i < len(words):
			words[i] = words[i].capitalize()
			i = i + 1

		print (' '.join(words))
 
if __name__ == '__main__':
	main()