with open("./data.txt") as f:
    lines = [int(i.strip()) for i in f.readlines()]

    a = [b > a for a, b in zip(lines, lines[1:])].count(True)
    print(a)

    n = 3
    b = [sum(lines[i+1:i+1+n]) > sum(lines[i:i+n]) for i in range(len(lines))][:-3].count(True)
    print(b)
