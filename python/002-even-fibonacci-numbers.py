total = 0
current = 1
prev = 1

while current < 4000000:
    temp = current
    current = current + prev
    prev = temp
    if current % 2 == 0:
        total += current

print (total)