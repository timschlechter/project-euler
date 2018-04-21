import math

def factors(n):
    results = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return results

x = 0
i = 0
while True:
    x += i
    if len(factors(x)) > 500:
        print(x)
    i += 1
