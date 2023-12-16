
content = open("./data.txt").read()

cache:dict[str,int] = {}

def get_hash(line:str, nums:list[int], past:str):
    return line + "-" + ",".join([str(i) for i in nums]) + "-" + past

def save(h, count):
    global cache
    cache[h] = count

def get_cached(h ) -> int | None:
    return cache.get(h)

def get_count(line:str, nums:list[int], past="."):

    cached = get_cached(get_hash(line, nums, past))
    if cached is not None:
        return cached
        
    if len(line) == 0 or len(nums)==0:
        if len(nums) ==0 and "#" not in line:
            return 1
        if len(line) == 0 and len(nums)==0:
            return 1
        return 0

    if line[0] == ".":
        return get_count(line[1:], nums, ".")

    if line[0] == "#":
        if past == "#":
            return 0
        reps = nums[0]
        for i in range(reps):
            if i >= len(line):
                return 0
            if line[i] == ".":
                return 0
        return get_count(line[reps:], nums[1:], "#")

    if line[0] == "?":
        if past == "#":
            return get_count(line[1:], nums, ".")
        line_a = "." + line[1:]
        line_b = "#" + line[1:]
        a = get_count(line_a, nums, past)
        b = get_count(line_b, nums, past)
        save(get_hash(line_a,nums,past),a)
        save(get_hash(line_b,nums,past),b)

        return a + b
    return 1

lines = content.split("\n")
part1 = 0
part2 = 0
for i, line in enumerate(lines):
    chunks = line.split()
    s = chunks[0]
    nums = [int(i) for i in chunks[1].split(",")]
    part1 += get_count(s, nums )
    n = 5 
    s = "?".join( [s] * n)  
    nums = nums * 5
    part2 += get_count(s, nums)

print(part1)
print(part2)



