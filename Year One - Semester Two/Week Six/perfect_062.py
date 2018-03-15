import sys


def sumFac(n):
    total = []
    for i in range(1, n//2 + 1):
        if not n % i:
            total.append(i)

    return sum(total)


def isPerfect(n):
    return sumFac(n) == n


def main():
    for n in sys.stdin:
        print(isPerfect(int(n.strip())))

if __name__ == '__main__':
    main()
