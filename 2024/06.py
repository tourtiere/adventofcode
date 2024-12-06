content = open('data.txt').read()

grid = {(i,j): c for j, line in enumerate(content.split('\n')) for i,c in enumerate(line)}

def compute(pos:tuple[int,int] )-> int | None:
    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    dir_idx = 0
    visited = set()
    states = set() # for part 2
    while grid.get(pos):
        state = tuple((pos[0], pos[1], dir_idx))
        if state in states:
            return None
        states.add(state)
        visited.add(pos)
        dx, dy = directions[dir_idx]
        next_pos = pos[0] + dx, + pos[1] + dy
        if grid.get(next_pos) == '#':
            dir_idx = (dir_idx + 1) % 4
        else:
            pos = next_pos
    return len(visited)

init_pos = [pos for pos, c in grid.items() if c == '^'][0]
print(compute(init_pos)) # part1
part2 = 0
for pos, c in grid.items():
    if c == ".": 
        grid[pos] = "#"
        if compute(init_pos) is None:
            part2 +=1
        grid[pos] = '.'
print(part2)