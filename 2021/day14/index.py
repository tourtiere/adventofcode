# from itertools import permutations, combinations
import re

with open("./data.txt") as f:
    content = f.read()
    data = {
        a: b
        for a, b in re.findall("(\\w\\w) -> (\\w)", content)
    }
    head = content.split("\n")[0]


s = {k: 0 for k in data.keys()}
count = {k: 0 for k in data.values()}

for i in range(len(head) - 1):
    s[head[i:i+2]] += 1


first, last = head[:2], head[-2:]

for i in range(40):

    first, last = first[0] + data[first], data[last] + last[1]

    new_s = {k: 0 for k in data.keys()}

    for k in data.keys():
        a, b = k[0] + data[k], data[k] + k[1]
        new_s[a] += s[k]
        new_s[b] += s[k]

    s = new_s

count = {k: 0. for k in data.values()}
for k in s.keys():
    count[k[0]] += s[k]
    count[k[1]] += s[k]


for k in count.keys():
    count[k] = count[k] / 2
    if k == first[0]:
        count[k] += 0.5
    if k == last[1]:
        count[k] += 0.5

print(first, last)
print(max(count.values()) - min(count.values()))
