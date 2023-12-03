with open("./data.txt") as f:
    content = f.read()
    lines = content.split("\n")
    grid = { (i, j):c for j, line in enumerate(lines) for i, c in enumerate(line)}
    s1 = 0

    gears = {k:[] for k in grid}

    for j, line in enumerate(lines):
        number = ""
        for i, letter in enumerate(line):
            if not letter.isdigit():
                number = ""
                continue
            number += letter
            succ = grid.get((i+1, j))
            if succ is None or not succ.isdigit():
                adj_keys = [(i+1-k, j-1) for k in range(len(number)+2) ]
                adj_keys += [(i+1-k, j+1) for k in range(len(number)+2) ]
                adj_keys += [(i+1, j), (i - len(number), j)]
                adj_values = [grid.get(n) for n in adj_keys] 
                alone = all([v is None or v == "." for v in adj_values ])

                if not alone:
                    s1 +=int(number)

                for key, value in zip(adj_keys, adj_values):
                        if (value=="*"):
                            gears[key].append(int(number))

    gear_ratios = sum([gears[g][0]*gears[g][1] for g in gears if len(gears[g]) ==2])
    print(s1)
    print(gear_ratios)
