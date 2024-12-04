lines = open('data.txt').read().split('\n')
mat = [ [c for c in row] for row in lines ]
M = len(mat)
N = len(mat[0])
G = {(i,j):mat[j][i] for j in range(M) for i in range(N) }
part1 = 0
part2 = 0
for j in range(M):
    for i in range(N):
        # part1
        for fx,fy in [(0,1), (1,1), (1,0), (1,-1)]:
            letters = [G.get((i + d * fx , j + d * fy)) for d in range(4)]
            if not all(letters): continue
            word = ''.join(letters)
            if 'XMAS'== word or 'SAMX' == word:
                part1 +=1
        # part2
        a =[ G.get((i + dx , j + dy)) for dx,dy in [(-1,-1), (0,0), (1,1)]]
        b =[ G.get((i + dx , j + dy)) for dx,dy in [(-1,1), (0,0), (1,-1)]]
        if not all(a) or not all(b): continue
        word_a, word_b = ''.join(a), ''.join(b)
        if (word_a == 'SAM' or word_a == 'MAS') and (word_b == 'SAM' or word_b == 'MAS'):
            part2 +=1
print(part1)
print(part2)