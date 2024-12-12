content = open('data.txt').read()
lines = content.split('\n')

grid = {(i,j):lines[j][i] for j in range(len(lines)) for i in range(len(lines[0]))}

def flood_fill(pos: tuple[int, int], group:set, fences:list ):
    x, y = pos
    for dx, dy in [(-1,0), (0,-1), (1,0), (0,1)] :
        p = x + dx, y + dy
        if p in group: continue
        if grid[pos] == grid.get(p):
            group.add(p)
            flood_fill(p, group, fences)
        else:
            fences.append((x,y, dx,dy))

def count_sides(fences):
    count = 0
    group = set({fences.pop()})
    while len(fences) > 0:
        subgroup = [f for f in fences if any( abs(g[0]-f[0])+ abs(g[1]-f[1]) == 1 and g[2] == f[2] and g[3] == f[3] for g in group ) and f not in group ]
        for s in subgroup:
            group.add(s)
            fences.remove(s)
        if len(subgroup) == 0:
            count += 1
            group = set({fences.pop()})
    return count + 1

def main():
    keys = set(grid.keys())
    part1 = 0
    part2 = 0
    while len(keys) > 0:
        k = keys.pop()
        area = set({k})
        fences = []
        flood_fill(k, area, fences)
        keys.difference_update(area)
        part1 += len(area) * len(fences)
        part2 += len(area) * count_sides(fences)
    print(part1)
    print(part2)
main()