current = 1
prev = 0
target = 10**999
i = 1

while current < target:
    tmp = current
    current = current + prev
    prev = tmp
    i += 1

print(i)