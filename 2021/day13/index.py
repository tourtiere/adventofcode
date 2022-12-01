# from itertools import permutations, combinations
import re


def print_s(s):
    t = ""
    for i in s:
        for j in i:
            if j:
                t += "#"
            else:
                t += "."
        t += "\n"
    print(t)


def reverse_m(m):
    M = []
    for j in range(len(m[0])):
        line = []
        for i in range(len(m)):
            line.append(m[i][j])
        M.append(line)
    return M


def fold(s, x):
    n = []
    for line in s:
        A, B = line[0:x], reversed(line[x:])
        n.append([a or b for a, b in zip(A, B)])
    return n


with open("./data.txt") as f:
    # l = re.findall("\\d+", f.read())

    data = []
    data = [line.split(",") for line in f.read().split("\n")][:-1]
    data = [(int(x), int(y)) for y, x in data]

max_x = max([x for x, y in data]) + 1
max_y = max([y for x, y in data]) + 1

s = [
    [False for _ in range(max_y)]
    for _ in range(max_x)
]
# init
for i, j in data:
    s[i][j] = True

fold_points = [["x", 655], ["y", 447], ["x", 327], ["y", 223], ["x", 163], [
    "y", 111], ["x", 81], ["y", 55], ["x", 40], ["y", 27], ["y", 13], ["y", 6]]


count = sum([i.count(True) for i in s])
print(count)

for axis, pos in fold_points:
    if (axis == "x"):
        s = fold(s, pos)
    else:
        s = reverse_m(fold(reverse_m(s), pos))

count = sum([i.count(True) for i in s])
print_s(s)
