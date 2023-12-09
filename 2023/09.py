
content = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

with open("./data.txt") as f:
    content = f.read()
    lines = content.split("\n")
    part1 = 0
    part2 = 0
    for line in lines:
        nums = [int(i) for i in line.split()]
        pyramid = [[n for n in nums]]

        while not all([n ==0 for n in pyramid[-1]]) :
            row = [b - a for a, b in zip(pyramid[-1], pyramid[-1][1:] )]
            pyramid.append(row)

        firsts = [row[0] for row in pyramid]
        lasts = [row[-1] for row in pyramid]

        first_first = 0
        last_last = 0
        for first, last in zip(reversed(firsts), reversed(lasts)):
            first_first = first - first_first
            last_last = last + last_last

        part1 += last_last
        part2 += first_first

    print(part1)
    print(part2)

