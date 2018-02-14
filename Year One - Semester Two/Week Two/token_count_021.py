import sys


def token_count(list):
    return len(list)


def main():
    total = 0
    for line in sys.stdin:
        tokens = line.strip().split()
        total = total + token_count(tokens)

    print(total)

if __name__ == '__main__':
    main()
