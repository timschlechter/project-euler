import math

for a in range(1, 500):
    for b in range(1, 500):
        c = math.sqrt(a * a + b * b)
        if c % 1 == 0 and a + b + c == 1000:
            print(a * b * c)
