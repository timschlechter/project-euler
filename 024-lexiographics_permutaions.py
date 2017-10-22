def permutate(items):
    if len(items) == 2:
        yield items
        yield [items[1], items[0]]
    else:
        for i in items:
            other = list(items)
            other.remove(i)
            for j in permutate(other):
                yield [i] + j


count = 0
for i in permutate(range(0, 10)):
    count += 1
    if count == 1000000:
        print(i)