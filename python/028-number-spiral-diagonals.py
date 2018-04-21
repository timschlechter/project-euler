result = 1
current = 1
for side_len in range(3, 1002, 2):
    for i in range(0, 4):
        current += side_len - 1
        result += current
        
print(result)