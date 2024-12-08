content = open('data.txt').read()

lines = content.split("\n")
R = len(lines)
C = len(lines[0])
groups = ()

grid = { (i,j): lines[j][i] for j in range(R) for i in range(C)}
digits = set(grid.values())

digits.remove('.')

part1 = set()
part2 = set()

def add(a,b) -> tuple[int,int]:
    return a[0] + b[0], a[1] + b[1]

def sub(a,b) -> tuple[int,int]:
    return a[0] - b[0], a[1] - b[1]

for d in digits:
    antenas = set(pos for pos, value in grid.items() if value == d)
    for pos1 in antenas:
        for pos2 in antenas:
            diff = sub(pos2, pos1)
            if diff[0] == 0 and diff[1] == 0: continue
            p = pos1
            part1.add(sub(p,diff))
            while grid.get(p):
                p = sub(p, diff)
                part2.add(p)
            p = pos2
            part1.add(add(p,diff))
            while grid.get(p):
                part2.add(p)
                p = add(p, diff)

part1 = {pos for pos in part1 if grid.get(pos)}
part2 = {pos for pos in part2 if grid.get(pos)}

print(len(part1))
print(len(part2))
