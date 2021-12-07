pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def fuel(position, idx):
    n = abs(position - idx)
    # problem a
    # return n

    # problem b
    return n * (n+1) // 2


m = min([
    sum([fuel(p, i) for p in pos])
    for i in range(len(pos))
])

print(m)
