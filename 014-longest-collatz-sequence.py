target = 1000000
chains = {}
longest = 0
longest_start = 0

for x in range(1, target):
    if x % 10000 == 0:
        print(x)
    n = x
    chain = []
    while n != 1:
        if n in chains:
            chain = chain + chains[n]
            break
        else:
            n = (int)(n / 2 if n % 2 == 0 else 3 * n + 1)
            chain.append(n)

    for c in range(0, len(chain)):
        chains[c] = chain[-c:]

    print(chains)
    if len(chain) > longest:
        longest = len(chain)
        longest_start = x
print(chains)
print(longest_start)