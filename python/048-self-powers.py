from functools import reduce

powers = map(lambda x: x**x, range(1, 1001))
summation = reduce(lambda x, y: x + y, powers)
last10 = str(summation)[-10:]

print(last10)
