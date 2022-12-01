with open("./data.txt") as f:

    blocks = f.read().split("\n\n")
    cals = []
    for block in blocks:
        lines = block.split("\n")
        lines = [int(line) for line in lines if line != ""]
        cals.append(sum(lines))

    cals = sorted(cals, reverse=True)
    print(sum(cals[:3]))
