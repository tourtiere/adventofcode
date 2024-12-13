content = open('data.txt').read()
import re 

for correction in [0, 10000000000000]:
    total = 0
    for block in content.split("\n\n"):
        x1, y1, x2, y2, X, Y = [int(i) for i in re.findall(r'\d+', block)]
        X += correction
        Y += correction
        # [ (A * x1 + B * x2) == X and (A * y1 + B * y2) == Y ] => 
        B = (x1 * Y - X * y1)/(x1 * y2 - x2 *y1)
        A = (x2 * Y - X * y2)/(x2 * y1 - x1 *y2)
        if round(A) == A and round(B) == B:
            total += 3 * A + B
    print(round(total))
