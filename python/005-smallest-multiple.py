def f(x):
    for i in reversed([20, 19, 18, 17, 16, 15, 14, 13, 12, 11]):
        if x % i != 0:
            return False
    return True


i = 20
while f(i) == False:
    i += 20
print(i)
