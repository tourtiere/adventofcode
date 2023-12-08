import math
import re

Matches = dict[str, list[str]]

def fn(matches:Matches, directions: str, init_step:int, init_value:str, part2:bool):
    steps = init_step
    value = init_value
    while True:
        direction = directions[steps % len(directions)]
        if direction == "L":
            value = matches[value][0]
        else:
            value = matches[value][1]
        steps +=1

        if (not part2 and value =="ZZZ"):
            return steps
        if (part2 and value[2] =="Z"):
            return steps

with open("./data.txt") as f:
    content = f.read().split("\n\n")
    directions = content[0] 
    lines = content[1].split("\n")
    lines = [re.findall(r"\w+",l) for l in lines]
    M = {line[0] : line[1:] for line in lines}

    steps = fn(M, directions, 0, "AAA", False)
    print(steps)
    
    nodes =[node for node in M if node[2] == "A" ]
    steps = [fn(M, directions, 0, node, True)  for node in nodes]
    print(math.lcm(*steps))
