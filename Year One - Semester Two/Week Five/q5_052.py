import sys


def main():
    skipped = []
    names = []
    markz = []

    for line in sys.stdin:

        n_marks = []
        [name, marks] = line.strip().split(':')

        try:
            for mark in marks.split(','):
                n_marks.append(int(mark))

            overall_mark = sum(n_marks)
            names.append(name)
            markz.append(overall_mark)

        except ValueError:
            skipped.append(name)
            continue

    values = [value for value, _ in sorted(zip(markz, names))[::-1]]
    name = [nam for _, nam in sorted(zip(markz, names))[::-1]]

    i = 0
    while i < len(values):
        print('{} : {}'.format(name[i], values[i]))
        i = i + 1

    if skipped:
        print('Skipped:')
        for name in skipped:
            print(name)

if __name__ == '__main__':
    main()
