import sys


for line in sys.stdin:
    [a, b, c, d] = line.strip().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    a = a + d
    score_a = a**2 + b**2 + c**2 + (7 * min(a,b,c))
    a = a - d

    b = b + d
    score_b = a**2 + b**2 + c**2 + (7 * min(a,b,c))
    b = b - d

    c = c + d
    score_c = a**2 + b**2 + c**2 + (7 * min(a,b,c))
    c = c - d


    if max(score_a, score_b, score_c) == score_a:
    	a = a + d

    elif max(score_a, score_b, score_c) == score_b:
    	b = b + d

    elif max(score_a, score_b, score_c) == score_c:
    	c = c + d

    score = a**2 + b**2 + c**2 + (7 * min(a,b,c))


    print(score)