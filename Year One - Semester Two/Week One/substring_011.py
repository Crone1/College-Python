import sys

def main():
	for line in sys.stdin:
		words = line.split()
		print(str(words[0].upper()) in str(words[1].upper()))
 
if __name__ == '__main__':
	main()