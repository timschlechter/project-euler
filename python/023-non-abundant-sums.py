from functools import reduce
from math import ceil, sqrt

def divisors(n):
    for i in  range(1, int(ceil(sqrt(n)))+1):
        if (n % i == 0):
            yield i

def abundant(n):
    return reduce((lambda x, y: x + y), divisors(n)) > n
    
abundants = filter(lambda x: abundant(x),range(12, 28124/2 + 1))

print(list(divisors(12)))