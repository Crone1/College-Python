import sys


def pallindrome_checker(line):
    return line == line[::-1]


def replace_full_stops(line):
    list = ['.', ',', ':', '_', '-', ';', '?', '/', '@', '#', '&']
    i = 0
    while i < len(list):
        line = line.replace(list[i], '')
        i = i + 1
    return line


def main():
    for line in sys.stdin:
        line = replace_full_stops(line)
        universal_string = ''.join(line.strip().lower().split())
        print(pallindrome_checker(universal_string))

if __name__ == '__main__':
    main()
