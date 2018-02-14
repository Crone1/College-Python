import sys


def remove_punctuation(line):
    lists = ['.', ',', ':', '_', '-', ';', '?', '/', '@', '#', '&']
    i = 0
    while i < len(lists):
        line = line.replace(lists[i], '')
        i = i + 1
    return line


def unique_checker(words):
    seen = []
    total = 0
    i = 0
    while i < len(words):
        if words[i].isdigit() or words[i].isalpha() and words[i] not in seen:
            seen.append(words[i])
            total = total + 1

        i = i + 1

    return total


def main():
    total = 0
    line = remove_punctuation(sys.stdin.read())
    tokens = line.strip().lower().split()
    total = total + unique_checker(tokens)
    print(total)

if __name__ == '__main__':
    main()
