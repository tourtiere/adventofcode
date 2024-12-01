import re
ex = '''3   4
4   3
2   5
1   3
3   9
3   3'''

from collections import defaultdict

with open("./in.txt") as f :
    content = ex
    content = f.read()
    lines = [[int(i) for i in re.findall(r'\d+', row)] for row in content.split("\n")]
    A, B = zip(*lines)
    A = sorted(A)
    B = sorted(B)
    distances = [abs(a-b) for a,b in zip(A,B)]
    part1 =sum(distances)
    print(part1)
    counts = defaultdict(int)
    for b in B:
        counts[b]+=1
    part2 = sum([a * counts[a] for a in A])
    print(part2)


