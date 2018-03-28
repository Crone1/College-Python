import sys

d = sys.argv[1]


def get_words(d_file):
    with open(d_file, 'r') as df:
        words = [line.strip() for line in df.readlines()]
        print(words)

    return words


def get_lines(file):
    with open(file, 'r') as f:
        copy = [c for c in f.readlines()]
        line_1 = [line[0:4] for line in copy]
        line_2 = [line[4:8] for line in copy]
        line_3 = [line[8:12] for line in copy]
        line_4 = [line[12:16] for line in copy]

        column_1 = [line.strip()[::4] for line in copy]
        column_2 = [line.strip()[1::4] for line in copy]
        column_3 = [line.strip()[2::4] for line in copy]
        column_4 = [line.strip()[3::4] for line in copy]

        diag_left_1 = [line[2::3] for line in copy]
        diag_left_2 = [line[3::3] for line in copy]
        diag_left_3 = [line[7::3] for line in copy]

        diag_right_1 = [line[1::5] for line in copy]
        diag_right_2 = [line[::5] for line in copy]
        diag_right_3 = [line[4::5] for line in copy]

        points = [0] * len(copy)

    return (line_1, line_2, line_3, line_4, column_1, column_2, column_3, column_4,
            diag_left_1, diag_left_2, diag_left_3, diag_right_1, diag_right_2,
            diag_right_3), points


def calculate_points(words, points):
    for word in words:
        #        print (word)
        if len(word) > 8:
            points += 11

        elif len(word) == 7:
            points += 5

        elif len(word) == 6:
            poins += 3

        elif len(word) == 5:
            points += 2

        elif len(word) == 3 or len(word) == 4:
            points += 1

    return points


def main():
    (lines_nd_columns_nd_diags, points) = get_lines(sys.argv[1])

    # print(lines_nd_columns_nd_diags)
#    print(points)

    num = 0
    while num < len(points):
        words = []
        print('________________________________________________')

        for lnc in lines_nd_columns_nd_diags:
            # print(lnc[num])
            for n in range(0, 5):
                for m in range(0, n):
                    # print(lnc[num][n:m])
                    if lnc[num][n:m] in get_words(d):
                        words.append(lnc[num][n:m])

                for m in range(n, 5):
                    # print(lnc[num][n:m])
                    if lnc[num][n:m] in d:
                        words.append(lnc[num][n:m])

        print(words)
        points[num] = calculate_points(words, points[num])
        print(points[num])

        num += 1


if __name__ == '__main__':
    main()
