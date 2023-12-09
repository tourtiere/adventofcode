def range_inter(r1, r2):
    return [ (a,b) for a,b in  [[max(r1[0], r2[0]), min(r1[1],r2[1])]] if a < b ]
    
def range_diff(r1, r2):
    return [ (a,b) for a,b in  [ [r1[0], r2[0]], [r2[1], r1[1]]] if a < b ]

with open("./data.txt") as f:
    content = f.read() 
    groups = content.split("\n\n")
    seeds = [int(i) for i in groups[0].split(":")[1].split()]
    range_seeds = [(seeds[i*2], seeds[i*2] + seeds[i*2+1]) for i in range(len(seeds)//2)]

    for group in groups[1:]:
        lines = group.split("\n")
        matches = [[int(i) for i in line.split()] for line in lines[1:]]
        offsets = [m[0] - m[1] for m in matches]
        match_ranges = [(m[1], m[1] + m[2]) for m in matches]

        for i in range(len(seeds)):
            seed = seeds[i]
            for offset, (a, b) in zip(offsets, match_ranges):
                if (a <= seed < b):
                    seeds[i] += offset

        i = 0
        new_range_seeds = []
        while i < len(range_seeds):
            range_seed = range_seeds[i]
            remaining = [] 
            for offset, (a, b) in zip(offsets, match_ranges):
                inters = range_inter(range_seed, (a,b))
                if (len(inters) > 0):
                    inter = inters[0]
                    range_seeds[i] = inter[0] + offset, inter[1] + offset
                    range_seeds += range_diff(range_seed, inter)
            i += 1

    print(min(seeds))
    print(min([r[0] for r in range_seeds]))
