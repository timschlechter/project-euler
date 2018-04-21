def is_prime(x, primes):
    for p in primes:
        if x % p == 0:
            return False
    return True

primes = [2]
i = 3
while len(primes) != 10001:
    if is_prime(i, primes):
        primes.append(i)
    i = i+1
    
print(primes[len(primes)-1])


      
    

