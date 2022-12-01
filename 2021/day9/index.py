import re

with open("./data.txt") as f:
    content = f.read()
    data = [
        [int(i) for i in line]
        for line in content.split("\n")[:-1]
    ]
    print(len(data), len(data[0]))


def get_neighbors(x, y):
    ns = [(x-1, y), (x+1, y), (x, y - 1), (x, y+1)]
    return [
        (i, j) for i, j in ns if
        (0 <= i and i < len(data))
        and
        (0 <= j and j < len(data[0]))
    ]


def is_point_low(x, y):
    point = data[x][y]
    if (point == 9):
        return False
    biggers = [i for i, j in get_neighbors(x, y) if point > data[i][j]]
    return len(biggers) == 0


def find_first_lows():
    lows = []
    for x, line in enumerate(data):
        for y, _ in enumerate(line):
            if is_point_low(x, y):
                lows.append((x, y))
    return lows


def find_connected_low(x, y, lows: list[tuple[int, int]]):
    if (data[x][y] == 9):
        return None

    if (x, y) in lows:
        return lows.index((x, y))

    for nx, ny in get_neighbors(x, y):
        if (data[x][y] > data[nx][ny]):
            idx = find_connected_low(nx, ny, lows)
            if not idx is None:
                return idx
    return None


lows = find_first_lows()

bassins = [0 for _ in lows]

for i, line in enumerate(data):
    for j, _ in enumerate(line):
        idx = find_connected_low(i, j, lows)
        if not idx is None:
            bassins[idx] += 1


product = 1
for i in sorted(bassins)[-3:]:
    product *= i
print(product)
