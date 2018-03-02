import sys


def check_following_characters(line1, line2, i, j):
    start_i = i
    start_j = j
    while i < len(line1) and j < len(line2) and line1[i] == line2[j]:
        i = i + 1
        j = j + 1

    return line1[start_i:i]


def main():
    [line1, line2] = sys.stdin.readlines()
    l1 = line1.strip()
    l2 = line2.strip()

    longest_substring = ''

    i = 0
    while i < len(l1):
        j = 0
        while j < len(l2):
            while j < len(l2) and l1[i] != l2[j]:
                j = j + 1

            if j < len(l2):
                substring = check_following_characters(l1, l2, i, j)
                if len(substring) > len(longest_substring):
                    index = j
                    longest_substring = substring

            j = j + 1

        i = i + 1

    print(longest_substring, len(longest_substring), index)

if __name__ == '__main__':
    main()
