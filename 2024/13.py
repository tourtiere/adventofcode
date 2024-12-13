content='''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''

content = open('data.txt').read()
import re 

part1 = 0

for block in content.split("\n\n"):
    x1, y1, x2, y2, X, Y = [int(i) for i in re.findall(r'\d+', block)]
    A, B = 0, 0
    min_price = float('inf')
    while A <= 100 and B <= 100 :
        condition1 = (A * x1 + B * x2) == X
        condition2 = (A * y1 + B * y2) == Y
        if (condition1 and condition2):
            price = 3 * A + B
            min_price = min(min_price, price)
        B += 1 
        if B > 100:
            B = 0
            A += 1
    if min_price != float('inf'):
        part1 += min_price

print(part1)

