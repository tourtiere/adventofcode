from collections import defaultdict
import heapq

content ='''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''
content2 = '''111111111111
999999999991
999999999991
999999999991
999999999991'''
content = open("./data.txt").read()

def add(a,b):
    return (a[0] + b[0]), (a[1] + b[1]),

lines = content.split("\n")
grid = { (i,j): int(c) for j, line in enumerate(lines) for i, c in enumerate(line)}
C = len(lines[0])
R = len(lines)


def solve_distances(distances, G):
    priority_queue:list[tuple[int,tuple]] = [(0, key) for key in distances if distances[key] ==0 ]
    heapq.heapify(priority_queue)

    while priority_queue:

        current_distance, current_key = heapq.heappop(priority_queue)

        if current_distance > distances[current_key]:
            continue

        for weight, adj_key in G[current_key]:
            adj_distance = current_distance + weight

            if distances.get(adj_key) is None or adj_distance < distances[adj_key]:
                distances[adj_key] = adj_distance
                heapq.heappush(priority_queue,(adj_distance, adj_key))
    return distances

def solve(start:tuple[int,int], end:tuple[int,int]):
    deltas = [(1,0), (-1,0), (0,1), (0,-1)]
    G = defaultdict(list)
    distances = { (node, tuple([a,b,c])):0 if node == start else float('infinity') for node in grid for a in deltas for b in deltas for c in deltas }
    for node_key in distances:
        node, current_deltas = node_key
        for delta in deltas:
            if current_deltas[-1][0] == -delta[0] and current_deltas[-1][1] == -delta[1]:
                continue
            if all([delta == current_delta for current_delta in current_deltas]) :
                continue
            adj = add(node, delta)
            new_deltas = list(current_deltas) + [delta]
            adj_key = (adj, tuple(new_deltas[-3:]))
            if adj not in grid:
                continue
            G[node_key].append((grid[adj], adj_key))
    solve_distances(distances,G)
    end_distances = [distances[key] for key in distances if key[0] == end]
    part1 = min(end_distances)
    print(part1)

    deltas = [(1,0), (-1,0), (0,1), (0,-1)]
    G = defaultdict(list)

    steps = [4,5,6,7,8,9,10]
    distances = { tuple([node, delta]):float('infinity') for node in grid for delta in deltas}
    distances[(start, (0,1))] = 0
    distances[(start, (0,-1))] = 0
    distances[(start, (1,0))] = 0
    distances[(start, (-1,0))] = 0

    for node_key in distances:
        node, prev_delta = node_key
        new_deltas = [delta for delta in deltas if delta != prev_delta and not( prev_delta[0] == -delta[0] and prev_delta[1] == -delta[1])]
        for delta in new_deltas:
            for i in steps:
                target_node = node[0] + i * delta[0], node[1] + i * delta[1]
                if target_node not in grid:
                    continue
                weight = 0
                for j in range(1, i+1):
                    weight += grid[node[0] + j * delta[0], node[1] + j * delta[1]]
                k = (weight, (target_node, delta))
                G[node_key].append(k)


    solve_distances(distances, G)
    end_distances = [distances[key] for key in distances if key[0] == end]
    print(min(end_distances))

solve((0,0), (C-1, R-1))
