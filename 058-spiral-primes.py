def get_corner_nrs(layer):
    if layer == 0:
        yield 1
    else:
        odd_square = side_len(layer) ** 2
        yield odd_square
        yield odd_square - layer * 2
        yield odd_square - layer * 4
        yield odd_square - layer * 6

def side_len(layer):
    return (layer + 1) * 2 - 1

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

primes = 0
nonprimes = 0

for layer in range(0, 1000000):
    for nr in get_corner_nrs(layer):
        if is_prime(nr):
            primes += 1
        else:
            nonprimes += 1
            ratio = primes / (primes + nonprimes) * 100
    if ratio < 10 and layer > 1:
        print(side_len(layer))
        break