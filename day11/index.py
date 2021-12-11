with open("./data.txt") as f:
    data = [[int(i) for i in line] for line in map(str.strip, f.readlines())]
    graph = {
        (i, j): data[i][j]
        for i in range(len(data))
        for j in range(len(data[0]))
    }


neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]


def flash(flashes: list[tuple[int, int]]):
    global graph
    new_flashes = [key for key in graph.keys() if graph[key] > 9 and key not in flashes]
    flashes += new_flashes

    for flash_idx in new_flashes:
        for n in neighbours:
            n_idx = (flash_idx[0] + n[0], flash_idx[1] + n[1])
            if n_idx in graph:
                graph[n_idx] += 1
        flashes = flash(flashes)

    return flashes


flash_count = 0
for i in range(100):
    graph = {
        idx: data + 1
        for idx, data in graph.items()
    }
    flashes = flash([])
    for f in flashes:
        graph[f] = 0
    flash_count += len(flashes)

    if (len(flashes) == len(graph.keys())):
        print("breakcount", i+1)
        break
print()
