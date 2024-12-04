from collections import defaultdict
lines = open('data.txt').read().split('\n')
mat = [ [c for c in row] for row in lines ]
R = len(mat)
C = len(mat[0])
G = defaultdict(str,{(i,j): mat[j][i] for j in range(R) for i in range(C) })
part1 = 0
part2 = 0
for j in range(R):
    for i in range(C):
        # part1
        for fx,fy in [(0,1), (1,1), (1,0), (1,-1)]:
            word = ''.join(G[(i + d * fx , j + d * fy)] for d in range(4))
            if word == 'XMAS' or word == 'SAMX':
                part1 +=1
        # part2
        a =''.join( G[(i + dx , j + dy)] for dx,dy in [(-1,-1), (0,0), (1,1)] )
        b =''.join( G[(i + dx , j + dy)] for dx,dy in [(-1,1), (0,0), (1,-1)] )
        if (a == 'SAM' or a == 'MAS') and (b == 'SAM' or b == 'MAS'):
            part2 +=1
print(part1)
print(part2)