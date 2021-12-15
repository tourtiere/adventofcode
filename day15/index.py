with open("./15.in") as f:

    lines = f.read().split("\n")[:-1]

    I = len(lines)
    J = len(lines[0])
    data = {(i, j): int(lines[i][j]) for j in range(J) for i in range(I)}

    data = {
        (i + delta_i * I, j + delta_j * J):
        (value + delta_i + delta_j)
        for (i, j), value in data.items()
        for delta_i in range(5)
        for delta_j in range(5)
    }

    data = {
        key: value if value < 10 else value - 9
        for key, value in data.items()
    }

# https://web.archive.org/web/20211125134952/https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Pseudocode


def dijkstra():

    Q = set(data.keys())

    dist = {i: float("inf") for i in Q}
    dist[(0, 0)] = 0

    prev: dict[tuple[int, int], tuple[int, int]] = {i: (0, 0) for i in Q}

    leaves = {(0, 0)}

    count = 0
    len_Q = len(Q)

    while len(Q) != 0:

        count += 1
        if (count % 1000 == 0):
            print(count / len_Q)

        u, value = (0, 0), float("inf")
        for leaf in leaves:
            if dist[leaf] < value:
                u, value = leaf, dist[leaf]

        leaves.remove(u)
        Q.remove(u)

        neighbors: list[tuple[int, int]] = [
            (u[0] + x, u[1] + y) for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]
        ]

        for v in neighbors:
            if v in Q:
                alt = dist[u] + data[v]
                if alt < dist[v]:
                    leaves.add(v)
                    dist[v] = alt
                    prev[v] = u

    return dist


dest = sorted(data.keys(), key=lambda k: k[0] * k[1])[0-1]

print(dijkstra()[dest])
