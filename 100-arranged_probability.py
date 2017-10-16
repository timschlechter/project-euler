import math

def f(x, y):
    return (x/y)*((x-1)/(y-1))

def test(blue, delta, discs):    
    P = f(blue, discs)
    if P == 0.5:
        print('P={0}, blue={1}, delta={2}'.format(P, blue, delta))
        return blue

    if delta == 1:
        return False

    delta = delta/2 if delta % 2 == 0 else (delta+1)/2
    
    if P > 0.5:
        return test(blue-delta, delta, discs)
    else:
        return test(blue+delta, delta, discs)

for discs in range(10**12, 10**13):
    blue = math.floor(discs / 2)
    if discs % 10**6 == 0:
        print(discs)
    #print(test(blue, blue, discs))    




# (x/y)*((x-1)/(y-1)) == 0.5
# y > 10**12

# 15,14 --> 21
# 85,84 --> 120