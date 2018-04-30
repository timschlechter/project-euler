# log(x^y) == y*log(x)

import math

with open('099-largest-exponential.txt') as f:    
    lines = map(lambda l: 
                 map(lambda d: int(d), l.split(',')),
                 f.readlines())

    lines = map(lambda l: l[1] * math.log(l[0]), lines)
                 
    print(lines.index(max(lines)) + 1)
