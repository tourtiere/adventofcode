# from itertools import permutations, combinations

with open("./data.txt") as f:
    data = [line.split("-") for line in f.read().split("\n")][:-1]
    graph = {}
    for a, b in data:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]


count = 0


def visit(path: list[str], twice: bool):
    global count
    last = path[-1]

    if last == "end":
        count += 1
        return

    for i in graph[last]:

        if i == "start":
            continue

        if (not i in path) or i.upper() == i:
            visit(path + [i], twice)

        if (i in path) and i.lower() == i and not twice:
            visit(path + [i], True)


visit(["start"], False)
print(count)
