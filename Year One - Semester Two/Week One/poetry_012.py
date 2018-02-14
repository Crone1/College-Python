iimport sys

def print_each_line(lines, longest):
	i = 0
	while i < len(lines):
		print ('{:^{}s}'.format(lines[i], longest - 1))
		i = i + 1

def main():
	longest = 0
	lines = []
	for line in sys.stdin:
		lines.append(line.strip())
		if len(line) > longest:
			longest = len(line)

	print_each_line(lines, longest)


if __name__ == '__main__':
	main()