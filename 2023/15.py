from collections import defaultdict

content = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
content = open("./data.txt").read()
content = "".join(content.split("\n"))
chunks = content.split(",")

def get_hash(s):
    h = 0
    for i in s:
        h += ord(i)
        h *= 17
        h = h % 256
    return h

part1 = [get_hash(i) for i in chunks]
print(sum(part1))


box_txt = defaultdict(list)
box_len = defaultdict(list)

for chunk in chunks:
    #print(chunk)

    def get_idx(s, h):
        if s in box_txt[h]:
            return box_txt[h].index(s)
        return -1

    s=chunk.split("=")
    if len(s) ==2:
        h = get_hash(s[0])
        i = get_idx(s[0], h)
        if i>=0:
            box_len[h][i] = int(s[1])
        else:
            box_txt[h].append(s[0])
            box_len[h].append( int(s[1]))

    if chunk[-1] == "-":
        s = chunk[:-1]
        h = get_hash(s)
        i = get_idx(s, h)
        if i >=0:
            box_txt[h].pop(i)
            box_len[h].pop(i)

part2 = 0
for i in range(256):
    part2 += sum([v * (i +1) *(j+1)for j,v in enumerate(box_len[i])])
print(part2)

