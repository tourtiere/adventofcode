def add(a,b):
    return (a[0] + b[0]), (a[1] + b[1]),

content = open("./data.txt").read()

max_path = []
lines = content.split("\n")
grid = {(i,j):c for j,line in enumerate(lines) for i,c in enumerate(line)}
start_pos = [xy for xy in grid if grid[xy] == "S"][0]

directions:dict[str, list[tuple[int,int]]] = {
    "|":[(0,-1), (0,1)],
    "-":[(-1,0), (1,0)],
    "L":[(0,-1), (1,0)],
    "J":[(0,-1), (-1,0)],
    "7":[(0,1), (-1,0)],
    "F":[(0,1), (1,0)],
    "S":[],
}

for d1 in [(-1,0), (0,-1), (1, 0), (0,1)]:
    v = grid.get(add(d1, start_pos))
    if v is not None:
        for d2 in directions[v]:
            if add(d1, d2) == (0,0):
                directions["S"] += [(-d2[0], -d2[1])]
                
def find_loop():
    coord = start_pos
    path = [start_pos, add(start_pos, directions["S"][0])]
    path_set = set(path)
    while True:
        coord = path[-1]
        for d in directions[grid[coord]]:
            adj = add(coord,d)
            if adj not in path_set:
                path_set.add(adj)
                path.append(adj)
            elif  adj == start_pos and len(path) > 3 :
                return path

arr = find_loop()
print(len(arr) // 2) # partie 1

flood_grid = {(x*3+i, y*3+j):False for x,y in grid for i in range(3) for j in range(3)}

for coord in arr:
    x = coord[0] * 3
    y = coord[1] * 3
    middle = add((x,y), (1,1))
    flood_grid[middle] = True
    char = grid.get(coord)
    for d in directions[grid[coord]]:
        flood_grid[add(middle, d)] = True

seed = (0,0)
lasts = [seed]
flood_grid[seed] = True

while len(lasts) != 0:
    new_lasts = []
    for last in lasts:
        for delta in [(-1,0), (1, 0), (0, -1), (0,1)]:
            adj = add(last, delta)
            adj_value = flood_grid.get(adj)
            if not adj_value:
                flood_grid[adj] = True
                new_lasts.append(adj)
    lasts = new_lasts

count = 0
for coord in grid:
    x = coord[0] * 3
    y = coord[1] * 3
    cells = [flood_grid[(x+i,y+j)] for i in range(3) for j in range(3)]
    if sum(cells) == 0:
        count +=1

print(count)

