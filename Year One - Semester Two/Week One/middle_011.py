import sys

def main():
	for line in sys.stdin:
		if len(line.strip()) % 2 == 0:
			print('No middle character!')

		else:
			print(line[len(line.strip()) // 2])
 
if __name__ == '__main__':
	main()