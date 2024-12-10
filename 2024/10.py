content = open('data.txt').read()

lines = content.split('\n')
C = len(lines[1]) 
R = len(lines)
grid = {(i,j): int(lines[j][i]) for j in range(R) for i in range(C)}

paths:dict[tuple[int,int], int] = {}
heads:dict[tuple[int,int], set[tuple[int,int]] ] = {}

def compute(pos: tuple[int,int]):
    if pos in heads:
        return
    if grid.get(pos) == 9:
        heads[pos] = set({pos})
        paths[pos] = 1
        return
    x,y = pos
    v = grid[pos]
    connected_heads = set()
    connected_paths = 0
    for dx,dy in [(0,-1), (1,0), (0,1), (-1, 0)]:
        p = x + dx, y + dy
        if p in grid and v + 1 == grid[p]:
            compute(p)
            connected_heads = connected_heads.union(heads[p])
            connected_paths += paths[p]
    heads[pos] = connected_heads
    paths[pos] = connected_paths

def main():
    for pos in grid.keys():
        compute(pos)
    print(sum(len(v) for k,v in heads.items() if grid[k] == 0))
    print(sum(v for k,v in paths.items() if grid[k] == 0))
main()

