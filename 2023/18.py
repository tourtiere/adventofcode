def add(a,b):
    return (a[0] + b[0]), (a[1] + b[1]),

def mul(a,n):
    return (a[0] * n), (a[1] * n),

content = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''
content = open("./data.txt").read()

def draw_grid(grid):
    min_x = min([i[0] for i in grid])
    min_y = min([i[1] for i in grid])

    max_x = max([i[0] for i in grid])
    max_y = max([i[1] for i in grid])

    s = ""
    for j in range(min_y, max_y+1):
        for i in range(min_x, max_x+1):
            if (i, j) == (0,0):

                s += "X"
            elif ((i,j) in grid):
                s += grid[(i,j)]
            else:
                s += "."
        s += "\n"
    return s

max_path = []
lines = content.split("\n")
pos = (0,0)
path = [(0,0)]
for line in lines:
    d, n, color = line.split()
    n = int(n)
    delta = {
        "L":(-1, 0),
        "R":(1, 0),
        "U":(0, -1),
        "D":(0, 1)
    }[d]

    for i in range(n):
        path.append(add(path[-1], delta))
# flood fill
grid = {p:"#" for p in path}
print(min([p[0] for p in path]))
print(min([p[1] for p in path]))
#print(draw_grid(grid))

flood_grid:dict[tuple[int,int],bool] = {p: False for p in grid}
seed = (1,1)
lasts = [seed]
flood_grid[seed] = True

while len(lasts) != 0:
    new_lasts = []
    for last in lasts:
        for delta in [(-1,0), (1, 0), (0, -1), (0,1)]:
            adj = add(last, delta)
            adj_value = flood_grid.get(adj)
            if adj_value is None:
                flood_grid[adj] = True
                new_lasts.append(adj)
    lasts = new_lasts

grid = {i: "#" for i in flood_grid if flood_grid[i]}
print(draw_grid(grid))
print(sum([ 1 for i in flood_grid if flood_grid[i]]) + len(path))

