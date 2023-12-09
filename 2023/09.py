
content = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

with open("./data.txt") as f:
    content = f.read()
    lines = content.split("\n")
    part1 = 0
    part2 = 0
    for line in lines:
        ns = [int(i) for i in line.split()]
        diff = [n for n in ns]
        lasts = [diff[-1]]
        firsts = [diff[0]]
        while not all([n ==0 for n in diff]) :
            diff = [b - a for a,b in zip(diff, diff[1:] )]
            lasts.append(diff[-1])
            firsts.append(diff[0])
            
        prev = 0
        hidden = []
        for last in reversed(lasts):
            hidden.append(last + prev) 
            prev = hidden[-1]
        part1 += prev

        prev = 0
        hidden = []
        for first in reversed(firsts):
            hidden.append(first - prev) 
            prev = hidden[-1]
        part2 += prev

    print(part1)
    print(part2)

