from dataclasses import dataclass

# for each (cell, velocity), find set of n energy block with n {n dependencies}
# foreach (cell, velocity), update from children
# repeat
# Dependencies list 
# !!  (get n dependencies (can be 1 ou 2 next)) = A get dependencies of A => B , rest = B - A, A= A + B, repeat

content ='''.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....'''
content = open("./data.txt").read()

matches = {
    "\\": lambda x,y: [(y, x)], 
    "/": lambda x,y: [(-y,-x)],
    "|": lambda x,y: [(x,y)] if x == 0 else [(0,1), (0,-1)],
    "-": lambda x,y: [(x,y)] if y == 0 else [(1,0), (-1,0)],
}

def add(a,b):
    return (a[0] + b[0]), (a[1] + b[1]),
 
@dataclass
class Cell:
    pos: tuple[int,int]
    v: tuple[int,int]

cells = [ Cell((0,0), (1,0))]
visited_positions:set[tuple[int,int]] = {(0,0)}

lines = content.split("\n")
grid = {(i,j):c for j, line in enumerate(lines) for i,c in enumerate(line)}


def draw():
    R = len(lines)
    C = len(lines[0])
    s = ""
    for j in range(R):
        for i in range(C):
            if (i,j) in visited_positions:
                s += '#'
            else:
                print((i,j))
                s += grid[(i,j)]
        s += "\n"
    print(s)

while len(cells) != 0:
    # update directions
    new_cells = []
    # update directions
    for cell in cells:
        cell_value = grid.get(cell.pos)
        if cell_value is None:
            continue
        visited_positions.add(cell.pos)
        if cell_value == ".":
            new_cells.append(cell)
            continue
        new_vs = matches[cell_value](*cell.v)
        for new_v in new_vs:
            new_cells.append(Cell(cell.pos, new_v))

    new_cells = [Cell(add(cell.pos, cell.v), cell.v) for cell in new_cells]
    cells = new_cells
    print(len((visited_positions)))
    #draw()

#print(len(visited_positions))
