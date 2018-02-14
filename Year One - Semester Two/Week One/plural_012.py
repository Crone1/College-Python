import sys

def plural_rules(x):
	vowls = ['a','e','i','o','u']

	if x[-2:] == 'ch' or x[-2:] == 'sh' or x[-1:] == 'x' or x[-1:] == 'z' or x[-1:] == 's' or x[-1:] == 'o':
		x = x + 'es'

	elif x[-1:] == 'f':
		x = x[:-1] + 'ves' 

	elif x[-2:] == 'fe':
		x = x[:-2] + 'ves'

	elif x[-1] == 'y' and x[-2] not in vowls:
		x = x[:-1] + 'ies'

	else:
		x = x + 's'

	return x

def main():
	for line in sys.stdin:
		print (plural_rules(line.strip()))

if __name__ == '__main__':
	main()