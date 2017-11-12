from functools import reduce

total = 0
with open('022-names.txt') as f:    
    names = sorted(f.read()[1:-1].split("\",\""))
    for idx, name in enumerate(names):
        total += (idx+1) * sum(map((lambda c: ord(c) - 64), name))

print(total)