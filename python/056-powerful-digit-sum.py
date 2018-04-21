from functools import reduce

maximum = 0

for a in range(1, 100):
    for b in range(1, 100):
        digits = map(lambda x: int(x), str(a**b))
        summation = reduce((lambda x, y: x + y), digits)
        maximum = max(maximum, summation)

print(maximum)
