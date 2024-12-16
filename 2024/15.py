content = open('data.txt').read()

def print_grid(grid):
    C = max([k[0] for k in grid.keys()]) + 1
    R = max([k[1] for k in grid.keys()]) + 1
    print('\n'.join([''.join(grid[(i,j)] for i in range(C)) for j in range(R)]))
 
def can_move(grid, x,y, dx,dy):
    c = grid.get((x,y))
    if c == '.':
        return True
    if c == '#':
        return False
    if dx == 0 and c == '[':
        return can_move(grid, x+dx,y+dy, dx,dy) and can_move(grid, x+1+dx,y+dy, dx,dy) 
    if dx ==0 and c == ']':
        return can_move(grid, x+dx,y+dy, dx,dy) and can_move(grid, x-1+dx,y+dy, dx,dy) 
    return can_move(grid, x+dx,y+dy, dx,dy)

def move(grid, x, y, dx, dy , propagate=True):
    c = grid.get((x,y))
    if c == '.': return
    if dx == 0 and c == '[' and propagate:
        move(grid, x + 1, y, dx,dy,False )
    if dx == 0 and c == ']' and propagate:
        move(grid, x - 1, y, dx,dy, False)
    move(grid, x+dx,y+dy, dx,dy)
    grid[(x + dx, y + dy)] = c
    grid[(x, y)] = '.'

def apply_moves(grid:dict[tuple[int,int], str], moves):
    pos = [p for p, v in grid.items() if v == '@'][0]
    for dx,dy in moves:
        if can_move(grid, *pos, dx,dy):
            assert grid[pos] == '@'
            move(grid, *pos, dx,dy )
            pos = pos[0] + dx, pos[1] + dy

def main():
    grid_content, move_content = content.split('\n\n')
    grid_lines = grid_content.split('\n')
    grid1 = {(i,j): grid_lines[j][i] for j in range(len(grid_lines)) for i in range(len(grid_lines[0]))}
    grid2 = {(i*2 + d, j): v for (i,j),v in grid1.items() for d in range(2)}
    for (i,j),v in grid2.items():
        if v == '@':
            if i %2 == 1:
                grid2[(i,j)] = '.'
        if v == 'O':
            if i%2 ==0:
                grid2[(i,j)] = '['
            else:
                grid2[(i,j)] = ']'

    moves:list[tuple[int,int]] = []
    for c in move_content:
        if c == "^": moves.append((0,-1))
        elif c == ">": moves.append((1,0))
        elif c == "<": moves.append((-1,0))
        elif c == "v": moves.append((0,1))

    apply_moves(grid1, moves)
    part1 = sum((j*100 + i) for (i,j),v in grid1.items() if v == 'O')
    print(part1)

    apply_moves(grid2, moves)
    part2 = sum((j*100 + i) for (i,j), v in grid2.items() if v == '[')
    print(part2)
main()



