def f(n):
    total = 0
    for c in str(n):
        total += int(c)**5
    return total

result = 0
for x in range(2, 1000000):
    if (f(x) == x):
        result += x
        print(x)

print(result)