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

def add(a,b):
    return (a[0] + b[0]), (a[1] + b[1]),

lines = content.split("\n")
grid = {(i,j):c for j, line in enumerate(lines) for i,c in enumerate(line)}


def get_count(ref_state):
    states = [ref_state]
    visited = set()
    while len(states) != 0:
        state = states.pop()
        visited.add(state)
        pos, v = state
        cell = grid.get(pos)
        x, y = v
        new_vs = [(x,y)]
        if cell is None:
            continue
        if cell == "\\":
            new_vs = [(y, x)]
        if cell == "/":
            new_vs = [(-y, -x)]
        if cell == "|":
            if x != 0:
                new_vs = [(0,1), (0,-1)]
        if cell == "-":
            if y != 0:
                new_vs = [(1,0), (-1,0)]

        for new_v in new_vs:
            new_pos = add(pos, new_v)
            if grid.get(new_pos) is None:
                continue
            new_state = (new_pos,new_v)
            if new_state not in visited:
                states.append(new_state)
    return len(set([state[0] for state in visited]))

print(get_count(((0,0), (1,0))))

R = len(lines)
C = len(lines[0])
max_value = 0

# from left
direction = (1,0)
i = 0 
for j in range(R):
    max_value = max(max_value, get_count(((i,j), direction)))

# from top
direction = (0,1)
j = 0 
for i in range(C):
    max_value = max(max_value, get_count(((i,j), direction)))

# from right
direction = (-1, 0)
i = C -1
for j in range(R):
    max_value = max(max_value, get_count(((i,j), direction)))

# from bottom
direction = (-1, 0)
j = R -1
for i in range(C):
    max_value = max(max_value, get_count(((i,j), direction)))

print(max_value)

