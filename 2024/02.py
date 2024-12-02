content = open('data.txt').read()
lines = [[int(i) for i in row.split()]for row in content.split("\n")]

def is_safe(l):
    inc = all(a<b for a,b in zip(l,l[1:]))
    dec = all(a>b for a,b in zip(l,l[1:]))
    absolutes = [abs(a-b) for a,b in zip(l,l[1:])]
    three = all(1 <= a and a <= 3 for a in absolutes)
    return (inc or dec) and three


part1 = sum([is_safe(line) for line in lines])
print(part1)

part2 = sum([ any( [is_safe(line[:i] + line[i+1:]) for i in range(len(line))]) for line in lines])
print(part2)