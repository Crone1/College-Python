import sys

for line in sys.stdin:
    [a, b, c] = line.strip().split()
    a = int(a)
    b = int(b)
    c = int(c)
    sqr_root = (b**2) - (4 * a * c)
    if sqr_root >= 0:
        plus_eq = (-b + ((sqr_root)**(1 / 2))) / (2 * a)
        minus_eq = (-b - (sqr_root)**(1 / 2)) / (2 * a)
        print('r1 = {}, r2 = {}'.format(plus_eq, minus_eq))
    else:
        print('None')
