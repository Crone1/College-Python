import sys

def each_character(x):
	a = {}
	for c in x:
		number_of_types = 0

		if c.isdigit():
			a['digit'] = 'here'
		elif c.isalpha():
			if c.isupper():
				a['uppercase'] = 'here'
			elif c.islower():
				a['lowercase'] = 'here'
		else:
			a['symbol'] = 'here'

	for key in a:
		if a[key] == 'here':
			number_of_types += 1

	return number_of_types

def main():
	for line in sys.stdin:
		print (each_character(line.strip()))

if __name__ == '__main__':
	main()