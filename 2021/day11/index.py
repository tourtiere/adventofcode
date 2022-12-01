with open("./data.txt") as f:
    data = [[int(i) for i in line] for line in map(str.strip, f.readlines())]
    graph = {
        (i, j): data[i][j]
        for i in range(len(data))
        for j in range(len(data[0]))
    }


def flash(flashes: list[tuple[int, int]]):
    global graph
    new_flashes = [key for key in graph.keys() if graph[key] > 9 and key not in flashes]
    flashes += new_flashes

    for flash_idx in new_flashes:
        for delta in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]:
            n = (flash_idx[0] + delta[0], flash_idx[1] + delta[1])
            if n in graph:
                graph[n] += 1
        flashes = flash(flashes)

    return flashes


flash_count = 0
for i in range(1, 2555):
    for idx in graph:
        graph[idx] += 1

    flashes = flash([])
    for f in flashes:
        graph[f] = 0
    flash_count += len(flashes)

    if (len(flashes) == len(graph.keys())):
        print("all", i)
        break
print()
