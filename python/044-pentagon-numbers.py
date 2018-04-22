from math import sqrt


def p(n):
    return n * (3 * n - 1) / 2


def is_p(n):
    return ((sqrt(24 * n + 1) + 1) / 6) % 1 == 0


D = float('inf')

for j in range(1, 10000):
    pj = p(j)
    for k in range(1, j - 1):
        pk = p(k)

        s = pj + pk
        d = pj - pk

        if (is_p(s) and is_p(d)):
            D = min(D, abs(pj - pk))
            print(D)
