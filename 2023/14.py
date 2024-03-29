content = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''

content = open("./data.txt").read()
lines = content.split("\n")

def transpose(grid):
    return {(y,x):grid[(x,y)] for x,y in grid}

def tilt_grid(old_grid, tilt_north=True):
    grid = {i: old_grid[i] for i in old_grid}
    x_len = max([i[0] for i in grid]) + 1
    y_len = max([i[1] for i in grid]) + 1


    for col_i in range(x_len):
        rolls = [k[1] for k in grid if k[0] ==col_i and grid[k] == "O"]
        rocks = [k[1] for k in grid if k[0] ==col_i and grid[k] == "#"]

        for j in rolls:
            grid[(col_i, j)] = "."

        for a,b in zip([-1]+ rocks, rocks + [y_len]):
            within = len([r for r in rolls if a < r and r < b])
            for i in range(within):
                k = (col_i, a+i+1)
                if not tilt_north:
                    k = (col_i, b-1-i )
                grid[k] = "O"


    return grid

def evaluate_grid(grid):
    y_len = max([i[1] for i in grid]) + 1
    return sum([y_len - k[1] for k in grid if grid[k] == "O"])

def draw_grid(grid):
    x_len = max([i[0] for i in grid]) + 1
    y_len = max([i[1] for i in grid]) + 1
    s = ""
    for j in range(y_len):
        for i in range(x_len):
            if ((i,j) in grid):
                s += grid[(i,j)]
            else:
                s += "."
        s += "\n"
    return s

def main():
    for is_part2 in [False, True]:
        grid = {(i,j):c for j, line in enumerate(lines) for i,c in enumerate(line)}
        n = 1
        if is_part2:
            n = 1000000000
        cache = {}
        i = 0
        while i < n:
            grid = tilt_grid(grid)
            if is_part2:
                grid = transpose(tilt_grid(transpose(grid)))
                grid = tilt_grid(grid, False)
                grid = transpose(tilt_grid(transpose(grid ), False))
            c = draw_grid(grid)
            i+=1
            if c in cache:
                cycle_length = (i - cache[c])
                cycles_to_go = (n - i) // cycle_length
                i += cycles_to_go * cycle_length
            cache[c] = i
        print(evaluate_grid(grid))

main()