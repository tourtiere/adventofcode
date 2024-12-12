content = open('data.txt').read()
lines = content.split('\n')

def adjacents(p: tuple[int,int]):
    return [ (delta, (p[0]+delta[0], p[1]+delta[1])) for delta in [(-1,0), (0,-1), (1,0), (0,1)] ]

grid = {(i,j):lines[j][i] for j in range(len(lines)) for i in range(len(lines[0]))}

def flood_fill(pos: tuple[int, int], group:set, fences:list, sides_count=0):
    sides = 0
    for delta, p in adjacents(pos):
        if p not in group and grid.get(p) == grid[pos]:
            group.add(p)
            sides += flood_fill(p, group, fences)
        elif grid.get(p) != grid[pos]:
            # [ for a,b in [(-1,0), (0,-1), (1,0), (0,1)]]
            fence = tuple([*pos, *delta])
            fences.append(fence)
    return sides + sides_count

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