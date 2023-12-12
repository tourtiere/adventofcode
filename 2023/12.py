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

def get_count(s:str, nums):
    count = 0
    unkowns = [i for i, c in enumerate(s) if c == "?"]
    already_count = sum([i == "#" for i in s])
    total = sum(nums)
    remaining = total - already_count
    count = 0
    for indexes in combinations(unkowns, remaining):
        test_line = list(s)
        for i in unkowns:
            test_line[i] = "."
        for i in indexes:
            test_line[i] = "#"

        dist = []
        for i in "".join(test_line).split("."):
            if i != "":
                dist.append(len(i))
        if dist == nums:
            count +=1

    return count

import math

def get_permute_nums(reps,nums):
    if len(nums) == 0:
        return 1
    n = reps
    n -= len(nums) - 1
    n -= sum(nums) - len(nums)
    k = len(nums)
    if n < 0:
        return 0
    return math.comb(n, k)

def get_count2(line:str, nums:list[int], count:int, past="."):

    if len(line) == 0 or len(nums)==0:
        if len(nums) == 0 and len(nums)==0:
            return count
        return 0

    if line[0] == ".":
        return get_count2(line[1:], nums, count, ".")

    if line[0] == "#":
        if past == "#":
            return 0
        reps = min(nums[0], len(line))
        for i in range(reps):
            if line[i] == ".":
                return 0
        return get_count2(line[reps:], nums[1:], count, "#")

    if line[0] == "?":
        if past == "#":
            return get_count2(line[1:], nums, count, ".")

        reps = 0
        for i in line:
            if i != "?":
                break
            reps +=1

        total = 0
        for pad in range(reps):
            for i in range(len(nums)):
                candidates = nums[:i]
                permutes = get_permute_nums(reps - pad -1, candidates)
                if permutes != 0:
                    total += permutes * get_count2(pad * "#" + line[(reps ):], nums[i:], count, ".")
        return total
        '''
        return sum([
            get_count2("." + line[1:], nums, count, past),
            get_count2("#" + line[1:], nums, count, past) ])
        '''

    return count

#print(get_permute_nums(5, [1, 2]))

#exit()
lines = content.split("\n")
part1 = 0
for i, line in enumerate(lines):
    chunks = line.split()
    res = []
    n =5 
    s = "?".join( [chunks[0]] * n)  
    nums = [int(i) for i in chunks[1].split(",") * n]
    #print(s,nums)
    count = get_count2(s, nums, 1)
    print(count)

#print(part1)



