import re
import math


content = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
with open("./data.txt") as f:
    content = f.read()
    lines = content.split("\n")
    grid = { (i, j):c for j,line in enumerate(lines) for i,c in enumerate(line)}
    s1 = 0

    gears = {k:[] for k, v in grid.items()}

    for j, line in enumerate(lines):
        number = ""
        for i in range(len(line)):
            letter = line[i]
            succ = grid.get((i+1, j))
            if (letter.isdigit()):
                number += letter
                if succ is None or not succ.isdigit():
                    neighbors = [(i+1-k, j-1) for k in range(len(number)+2) ]
                    neighbors += [(i+1-k, j+1) for k in range(len(number)+2) ]
                    neighbors += [(i+1, j), (i - len(number), j)]
                    values = [grid.get(n) for n in neighbors] 
                    seul = all([v is None or v == "." for v in values ])
                    print(seul, number)
                    #if all():
                    if not seul:
                        s1 +=int(number)

                    for n,value in zip(neighbors, values):
                        if (value=="*"):
                            gears[n].append(int(number))

            else:
                number = ""
    gear_ratios = sum([gears[g][0]*gears[g][1] for g in gears if len(gears[g]) ==2])
    print(s1)
    print(gear_ratios)
