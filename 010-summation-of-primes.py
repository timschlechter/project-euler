from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


primes = [2]
for i in range(3, 2000000):
    if i % 100000 == 0:
        print(i)

    if is_prime(i):
        primes.append(i)

summation = reduce((lambda x, y: x + y), primes)

print(summation)
