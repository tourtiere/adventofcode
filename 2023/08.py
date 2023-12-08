from os import DirEntry


content = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''

with open("./data.txt") as f:

    content = f.read().split("\n\n")
    #content = content.split("\n\n")
    directions = content[0] 
    lines = content[1].split("\n")
    lines = [[l[:3],l[7:10], l[12:15]]for l in lines]
    M = {line[0] : line[1:] for line in lines}

    value = "AAA"
    i = 0

    for j in range(10):
        counter = 0
        while (value := M[value][directions[i % len(directions)] == "R"])  != "ZZZ":
            i+=1
            counter +=1
        print(i % len(directions), counter)
