from itertools import permutations

with open("./data.txt") as f:
    lines = f.read().strip().split("\n")
    count = 0

    lines = [line.strip().split(" ") for line in lines]

    count = 0
    for x, y in lines:
        y = {"X": "A", "Y": "B", "Z": "C"}[y]
        count += {"A": 1, "B": 2, "C": 3}[y]

        win = any([x == "A" and y == "B", x == "B" and y == "C", x == "C" and y == "A"])
        draw = any([x == "A" and y == "A", x == "B" and y == "B", x == "C" and y == "C"])

        if win:
            count += 6
        elif draw:
            count += 3

    print(count)
