import re
#import math
from statistics import variance

def next_state(state, size:tuple[int,int]) :
    return [( (x + dx) % size[0], (y + dy) % size[1] , dx, dy) for x,y,dx,dy in state]

def print_grid(state, size) :
    s = set()
    for i,j,_,_ in state:
        s.add((i,j))
    lines = ['']
    for j in range(size[1]):
        lines.append('')
        for i in range(size[0]):
            lines[len(lines)-1] += '*' if (i,j) in s else ' '
    print('\n'.join(lines))


def main():
    content ='''p=0,4 v=3,-3
    p=6,3 v=-1,-3
    p=10,3 v=-1,2
    p=2,0 v=2,-1
    p=0,0 v=1,3
    p=3,0 v=-2,-2
    p=7,6 v=-1,-3
    p=3,0 v=-1,-2
    p=9,3 v=2,3
    p=7,3 v=-1,2
    p=2,4 v=2,-3
    p=9,5 v=-3,-3'''

    content = open('data.txt').read()
    size = 11, 7
    size = 101, 103

    lines = content.split("\n")

    init_state = []
    for line in lines:
        init_state.append([int(i) for i in re.findall(r'-*\d+', line)])

    states = init_state
    for i in range(100):
        states = next_state(states, size)

    quadrants = [0,0,0,0]
    for x,y,_,_ in states:
        split = size[0]//2, size[1]//2
        a, b  = None, None
        if x < split[0]:
            a = 0
        elif x >= split[0] + 1:
            a = 1
        if y < split[1]: 
            b = 0
        elif y >= split[1] + 1:
            b = 1
        if a is None or b is None: continue
        quadrants[a * 2 + b] += 1
    part1 = 1
    for q in quadrants:
        part1 *= q
    print(part1)

    # part2
    states = init_state
    i = 0
    while True:
        ints = sorted(list(set(y * size[0] + x for x,y, _,_ in states)))
        ones = [b - a for a,b in zip(ints, ints[1:])].count(1)
        if ones > 100:
            print_grid(states,size)
            print(i)
            exit()
        states = next_state(states, size)
        i +=1
main()
