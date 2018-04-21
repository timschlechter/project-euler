# https://www.daniweb.com/programming/software-development/code/216880/check-if-a-number-is-a-prime-number-python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

side_len = 1
current = 1
count = 1
primes = 0
ratio = 1

while ratio > 0.1:
    side_len += 2
    for i in range(0, 4):
        current += side_len - 1
        if i != 3 and is_prime(current):
            primes += 1
    count += 4
    ratio = primes / count    

print(side_len)
