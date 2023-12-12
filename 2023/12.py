from itertools import combinations
'''

branches = [1]
branch_idx = [0]

for each branch
    on ??? sequence, get all possible solutions for next ??, considering following ?? sequence
    find all possible matching indexes set, create branch for them
    multiply possible match to branch
    create 
'''

content = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''

#content = open("./data.txt").read()

def get_dash_dist(s:str):
    occ = []
    for i in s.split("."):
        if i != "":
            occ.append(len(i))
    return occ

lines = content.split("\n")
count = 0
for line in lines:
    chunks = line.split()
    chunks[0] *= 5
    chunks[1] = ",".join(5 * [chunks[1]])
    s = chunks[0]
    nums = [int(i) for i in chunks[1].split(",")]
    print(s, nums)
    unkowns = [i for i, c in enumerate(s) if c == "?"]
    already_count = sum([i == "#" for i in s])
    total = sum(nums)
    remaining = total - already_count
    '''
    for indexes in combinations(unkowns, remaining):
        test_line = list(s)
        for i in unkowns:
            test_line[i] = "."
        for i in indexes:
            test_line[i] = "#"
        compared = "".join(test_line)
        if get_dash_dist(compared) == nums:
            count += 1




    '''

