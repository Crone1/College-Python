import sys

filename = sys.argv[1]
joint_best = []

try:
    with open(filename, 'r') as f:
        marks_and_name = f.readlines()

        name = ''
        best = 0
        for line in marks_and_name:
            line = line.strip().split()
            try:
                if int(line[0]) > int(best):
                    best = int(line[0])
                    name = ' '.join(line[1:])

                elif int(line[0]) == best:
                    joint_best.append(' '.join(line[1:]) + ",")

            except ValueError:
                pass

    if len(joint_best) == 0:
        print('Best student(s): {}'.format(name))
        print('Best mark: {}'.format(best))

    else:
        print('Best student(s): {}, {}'.format(
            name, ' '.join(joint_best)[:-1]))
        print('Best mark: {}'.format(best))

except FileNotFoundError:
    print('The file {} could not be opened'.format(filename))

except ValueError:
    print('Invalid mark {} encountered. Exiting.'.format(
        marks_and_name[i].strip().split()[0]))
