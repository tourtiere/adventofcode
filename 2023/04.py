from collections import defaultdict

with open("./data.txt") as f:
    content = f.read() 
    lines = content.split("\n")
    part1 = 0
    scratches = defaultdict(int)
    R = len(lines)
    for i, line in enumerate(lines):
        scratches[i] += 1
        numbers = line.split(":")[1].split("|")
        winning, hand = [[int(i) for i in s.split()]  for s in numbers]
        score = 0
        matches = [n for n in hand if n in winning]
        if (len(matches) != 0):
            score =2**(len(matches)-1)

        for j in range(len(matches)):
            if i+j+1 < R:
                scratches[i+j+1] += scratches[i] 
        part1 += score
        
    print(part1)
    print(sum(scratches.values()))

