import sys

def print_each_line(lines, longest, club_names, other_details):
	i = 0
	while i < len(lines):
		print ('{:>3s} {:<{}s}{:>3s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}'.format(
		str(lines[i].split(' ')[0]), club_names[i].strip(), longest - 1, 
		str(other_details[i][0]), str(other_details[i][1]),
		str(other_details[i][2]), str(other_details[i][3]),
		str(other_details[i][4]), str(other_details[i][5]),
		str(other_details[i][6]), str(other_details[i][7].strip())))
		i = i + 1

def main():
	longest = 0
	lines = []
	other_details = []
	club_names = []
	characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'
	,'r','s','t','u','v','w','x','y','z',' ','A','B','C','D','E','F','G','H','I','J',
	'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	for line in sys.stdin:
		m = 0
		while m < len(line) and line[m].isdigit():
			m = m + 1

		j = m + 1
		while j < len(line) and line[j] in characters:
			j = j + 1

		name = line[m + 1:j]
		club_names.append(name)
		other_details.append(line[j:].split(' '))

		lines.append(line.strip())

		if len(name) > longest:
			longest = len(name)

	print ('{:>3s} {:<{}s}{:>3s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}'.format(
		'POS', 'CLUB', longest - 1, 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'PTS'))

	print_each_line(lines, longest, club_names, other_details)

if __name__ == '__main__':
	main()