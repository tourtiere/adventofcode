content='''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''

content = open("./data.txt").read()

def transpose(grid):
    return {(y,x):grid[(x,y)]for x,y in grid}

def get_reflections_rows(grid)->list[int]:
    rows = max([i[0] for i in grid]) + 1
    cols = max([i[1] for i in grid]) + 1
    reflections = []
    for j in range(0, cols-1):
        reflection =True
        for y1, y2 in zip(range(j,-1, -1 ), range(j+1, cols)):
            for i in range(rows):
                if grid[(i, y1)] != grid[(i, y2)]:
                    reflection = False
        if reflection:
            reflections.append(j+1)
    return reflections


def find_diff_refl(grid, prev_refls):
    for i in grid:
        prev = grid[i]
        grid[i] = { ".":"#","#":"."}[prev]
        refls = get_reflections_rows(grid)
        grid[i] = prev
        if len(refls) > 0 and refls != prev_refls:
            new_one = [r for r in refls if r not in prev_refls][0]
            return [new_one]
    return []

blocks = content.split("\n\n")
part1 = 0
part2 = 0
for block in blocks:
    grid = {(i,j):c for j,line in enumerate(block.split("\n")) for i,c in enumerate(line)}

    rows_refl = get_reflections_rows(grid)
    cols_refl = get_reflections_rows(transpose(grid))
    if len(rows_refl) > 0:
        part1 += 100 * rows_refl[0]
    if len(cols_refl) > 0:
        part1 += cols_refl[0]


    new_rows_refl = find_diff_refl(grid, rows_refl)
    new_cols_refl = find_diff_refl(transpose(grid), cols_refl)
    if len(new_rows_refl) > 0:
        part2 += 100 * new_rows_refl[0]
    if len(new_cols_refl) > 0:
        part2 += new_cols_refl[0]


print(part1)
print(part2)


