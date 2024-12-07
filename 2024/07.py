content = open('data.txt').read()

from __future__ import annotations
import re
from itertools import  product

def is_match(possible_ops: list[str], nums: list[str],target:str):
    for ops in product(possible_ops, repeat=len(nums)-1):
        result = 0
        for a, op in zip( nums, [''] + list(ops)):
            if op == '':
                result = int(a)
            elif op == "*":
                result *= int(a)
            elif op == "+":
                result += int(a)
            elif op == "||":
                result = int(str(result)  + a)
        if int(target) == result:
            return  True
    return False

part1 = 0
part2 = 0
for line in content.split("\n"):
    nums = [i for i in re.findall(r'\d+', line)]
    target = nums[0]
    nums = nums[1:]
    if is_match(['+', '*'], nums, target):
        part1 += int(target)
    if is_match(['+', '*', '||'], nums, target):
        part2 += int(target)

print(part1)
print(part2)