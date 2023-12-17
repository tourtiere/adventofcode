import heapq
from typing import DefaultDict

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
content = open("./data.txt").read()

def add(a,b):
    return (a[0] + b[0]), (a[1] + b[1]),

lines = content.split("\n")
grid = { (i,j): int(c) for j, line in enumerate(lines) for i, c in enumerate(line)}
C = len(lines[0])
R = len(lines)

'''
def draw(path:list[tuple[int,int]]):
    s = ""
    for j in range(R):
        for i in range(C):
            if (i,j) in path:
                s += "."
            else:
                s += str(grid[(i,j)])

        s +="\n"
    return s
'''

deltas_comb:list[list[tuple[int,int]]] =[]
deltas_adj:list[tuple[int,int]] = [(1,0), (-1,0), (0,1), (0,-1)]
for a in deltas_adj:
    for b in deltas_adj:
        for c in deltas_adj:
            deltas_comb.append([a,b,c])

from collections import defaultdict

Node = tuple[int, int]
def solve(start:tuple[int,int], end:tuple[int,int]):

    distances = {(node, tuple(d)): float('infinity') for node in grid for d in deltas_comb}
    for d in deltas_comb:
        distances[(start,tuple(d))] = 0

    priority_queue:list[tuple[int,tuple]] = [(0, key) for key in distances if distances[key] ==0] 
    heapq.heapify(priority_queue)

    while priority_queue:

        current_distance, current_key = heapq.heappop(priority_queue)
        current_node, current_deltas = current_key

        if current_distance > distances[current_key]:
            continue

        for delta in [(1,0), (-1,0), (0,1), (0,-1)]:
            adj = add(current_node, delta)
            weight = grid.get(adj)
            if weight is None:
                continue

            if current_deltas[-1][0] == -delta[0] and current_deltas[-1][1] == -delta[1]:
                continue

            if all([delta == current_delta for current_delta in current_deltas]) :
                continue

            new_deltas = list(current_deltas) + [delta]

            adj_key = (adj, tuple(new_deltas[-3:]))
            adj_distance = current_distance + weight

            if distances.get(adj_key) is None or adj_distance < distances[adj_key]:
                distances[adj_key] = adj_distance
                heapq.heappush(priority_queue,(adj_distance, adj_key))

    end_distances = [distances[key] for key in distances if key[0] == end]
    return min(end_distances)
    #return distances[end]

path = solve((0,0), (C-1, R-1))
print(path)
