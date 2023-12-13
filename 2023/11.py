content = open("./data.txt").read()
lines = content.split("\n")
grid = {(i,j):c for j,line in enumerate(lines) for i,c in enumerate(line)}

stars =  [i for i in grid if grid[i] == "#"]
xs = [s[0] for s in stars]
ys = [s[1] for s in stars]

rows = [i for i in range(max(xs) + 1) if i not in xs]
cols = [i for i in range(max(ys) + 1) if i not in ys]

def compute_distances(f):
    expanded = [(x + (f-1)* len([r for r in rows if x > r]), y + (f-1)*len([c for c in cols if y > c])) for x,y in stars ]
    distances = [abs(a[0] - b[0]) + abs(a[1] - b[1]) for a in expanded for b in expanded if a !=  b]
    return int(sum(distances)//2)

print(compute_distances(1))
print(compute_distances(1e6))
