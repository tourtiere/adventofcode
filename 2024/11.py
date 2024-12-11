from collections import defaultdict

data = '6 11 33023 4134 564 0 8922422 688775'

def compute(n, max_blink, cache, blink=0):
    res = 0
    if (n, blink) in cache:
        return cache[(n,blink)]
    elif blink == max_blink:
        res = 1
    elif len(str(n)) % 2 == 0:
        s = str(n)
        a, b = s[:len(s)//2], s[len(s)//2:]
        res = compute(int(a), max_blink, cache, blink +1) + compute(int(b), max_blink, cache, blink + 1)
    elif n == 0:
        res = compute(1,max_blink, cache, blink + 1)
    else:
        res = compute(n * 2024, max_blink, cache, blink + 1)
    cache[(n,blink)] = res
    return res

part1, part2 = 0, 0
cache1, cache2 = defaultdict(int), defaultdict(int)

for s in data.split():
    part1 += compute(int(s), 25, cache1)
    part2 += compute(int(s), 75, cache2)

print(part1)
print(part2)
