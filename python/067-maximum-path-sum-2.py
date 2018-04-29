with open('067-maximum-path-sum-2.txt') as f:    
    triangle = map(lambda l: 
                 map(lambda d: int(d), l.split(' ')),
                 f.readlines())

    prev_row = triangle[-1]
    rows = list(reversed(triangle[:-1]))

    for row in rows:
        for idx, val in enumerate(row):
            row[idx] = val + max(prev_row[idx], prev_row[idx+1])
        prev_row = row

    print(rows[-1])