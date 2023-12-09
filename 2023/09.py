with open("./data.txt") as f:
    content = f.read()
    lines = content.split("\n")
    part1 = 0
    part2 = 0
    for line in lines:
        nums = [int(i) for i in line.split()]
        pyramid = [[n for n in nums]]

        while any([n != 0 for n in pyramid[-1]]) :
            base = pyramid[-1]
            row = [b - a for a, b in zip(base, base[1:])]
            pyramid.append(row)

        first = 0
        last = 0
        for row in reversed(pyramid):
            first = row[0] - first
            last = row[-1] + last
            
        part1 += last
        part2 += first

    print(part1)
    print(part2)

