def squares_summed(x):
    return 1 if x == 1 else x*x + squares_summed(x-1)

def summed(x):
    return 1 if x == 1 else x + summed(x-1)

def sums_squared(x):
    total = summed(x)
    return total * total


print(sums_squared(100)-squares_summed(100))


      
    

