from collections import defaultdict

content = open('data.txt').read()
rules, pages = content.split('\n\n')
greater:dict[str, set[str]] = defaultdict(set) # greater[a] : set of all elements greater than a

for row in rules.split('\n'):
    a,b = row.split('|')
    greater[a].add(b)
 
part1 = 0
part2 = 0
for page in pages.split('\n'):
    l = page.split(',')
    is_ordered = all( b in greater[a] for a,b in zip(l, l[1:]))
    # part 1
    if is_ordered:
        part1 += int(l[len(l)//2])

    # part 2
    def cmp(a, b):
        if a in greater[b]: return 1
        elif b in greater[a]: return -1
        else: return 0
    import functools
    if not is_ordered:
        l = sorted(l, key= functools.cmp_to_key(cmp))
        part2 += int(l[len(l)//2])

print(part1)
print(part2)