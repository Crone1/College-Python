import sys

filename = sys.argv[1]

try:
    with open(filename, 'r') as f:
        marks_and_name = f.readlines()
        i = 1
        best = marks_and_name[0].strip().split()
        while i < len(marks_and_name):
            try:
                if int(marks_and_name[i].strip().split()[0]) > int(best[0]):
                    best = marks_and_name[i].strip().split()

            except ValueError:
                print('Invalid mark {} encountered. Skipping.'.format(
                    marks_and_name[i].strip().split()[0]))

            i = i + 1

    print('Best student: {}'.format(' '.join(best[1:])))
    print('Best mark: {}'.format(best[0]))

except FileNotFoundError:
    print('The file {} could not be opened'.format(filename))

except ValueError:
    print('Invalid mark {} encountered. Exiting.'.format(
        marks_and_name[i].strip().split()[0]))
