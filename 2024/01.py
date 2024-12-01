import re
from collections import defaultdict

content = open('data.txt').read()
lines = re.findall(r'(\d+)\s+(\d+)', content)
A = sorted([int(a) for a,b in lines])
B = sorted([int(b) for a,b in lines])
distances = [ abs(a-b) for a,b in zip(A,B) ]
part1 =sum(distances)
print(part1)
counts = defaultdict(int)
for b in B:
    counts[b]+=1
part2 = sum([a * counts[a] for a in A])
print(part2)