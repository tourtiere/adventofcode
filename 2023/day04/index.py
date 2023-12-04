import re 

with open("./data.txt") as f:
    content =f.read() 
    lines = content.split("\n")
    part1=0
    part2=0
    scratches = {i:1 for i,_ in enumerate(lines)}
    R = len(lines)
    for i, line in enumerate(lines):
        numbers = line.split(":")[1].split("|")
        winning, hand = [[int(i) for i in re.findall(r"\d+", s)]  for s in numbers]
        score= 0
        matches = [n for n in hand if n in winning]
        if (len(matches) != 0):
            score =2**(len(matches)-1)

        for j in range(len(matches)):
            if i+j+1 < R:
                scratches[i+j+1] += scratches[i] 
        part2 += scratches[i]
        part1 += score
        
    print(part1)
    print(part2)
