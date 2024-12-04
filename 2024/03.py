import re
content = open('data.txt').read()
lines = re.findall(r'mul\((\d{1,3})\,(\d{1,3})\)',content)
part1 = sum(int(a) * int(b) for a,b in lines)
print(part1)
lines = re.findall(r'mul\((\d{1,3})\,(\d{1,3})\)|(do\(\))|(don\'t\(\))',content)
part2 = 0
enable = True
for a, b, do, dont in lines:
    if enable and (a or b):
        part2 += int(a) * int(b)
    elif do:
        enable = True
    elif dont:
        enable = False
print(part2)
