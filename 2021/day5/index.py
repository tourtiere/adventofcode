import re


def print_grid(grid):
    return "\n".join([
        "".join([
            ("." if x == 0 else str(x)) for x in line
        ]) for line in grid
    ])


grid_len = 1000
grid = [[0 for _ in range(grid_len)] for _ in range(grid_len)]

with open('data.txt') as f:
    matches = re.findall("(\\d+),(\\d+) -> (\\d+),(\\d+)", f.read())
    points = [[int(i) for i in match] for match in matches]

# problem a filter
# points = [point for point in points if point[0] == point[2] or point[1] == point[3]]

for x, y, xp, yp in points:

    line_size = max(abs(xp - x), abs(yp - y))

    for i in range(line_size + 1):
        m = x + i * int((xp - x) / line_size)
        n = y + i * int((yp - y) / line_size)
        grid[n][m] += 1

grid_count = len([x for line in grid for x in line if x >= 2])
print(grid_count)
