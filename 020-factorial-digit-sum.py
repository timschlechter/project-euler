def f(x):
    return x * f(x-1) if x >= 2 else x

f100 = f(100) 

total = 0
for d in str(f100):
    total += int(d)

print(total)