import math

target = 600851475143

for x in range(1, math.ceil(math.sqrt(target))):
    if x % 2 == 1 and x % 5 != 0:
        if target % x == 0:
            print (x)
