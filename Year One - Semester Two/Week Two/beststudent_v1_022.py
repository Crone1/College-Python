import sys

filename = sys.argv[1]

try:
	with open(filename, 'r') as f:
		marks_and_name = f.readlines()
		i = 1
		best = marks_and_name[0].strip().split()
		while i < len(marks_and_name):
			if marks_and_name[i].strip().split()[0] > best[0]:
				best = marks_and_name[i].strip().split()
			i = i + 1

	print ('Best student: {}'.format(' '.join(best[1:])))
	print ('Best mark: {}'.format(best[0]))

except FileNotFoundError:
	print ('The file {} could not be opened'.format(filename))