from functools import reduce

known = {}
counter = 0


def f(n, chain):
    if (known.get(n) == 89 or known.get(n) == 1):
        n = known.get(n)

    if (n == 89 or n == 1):
        for x in chain:
            known[x] = n
            return n == 89

    chain.append(n)

    digits = map(lambda c: int(c) * int(c), str(n))
    next = reduce((lambda x, y: x + y), digits)
    return f(next, chain)


for n in range(1, 10000000):
    if (f(n, list())):
        counter += 1

print(counter)
