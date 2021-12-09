import itertools


with open("./data.txt") as f:
    data = [
        line.split(" ")
        for line in f.read().split("\n")[:-1]
    ]

based_digits = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

result = []
for digits in data:
    digits.remove("|")
    for a, b, c, d, e, f, g in itertools.permutations("abcdefg", 7):
        letters_map = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g}
        rearranged_digits = [
            "".join(sorted([letters_map[d] for d in digit]))
            for digit in digits
        ]
        if len([digit for digit in rearranged_digits if digit in based_digits]) == len(digits):
            n = [based_digits.index(output) for output in rearranged_digits[-4:]]
            n = int("".join([str(d) for d in n]))
            result.append(n)
            break
print(sum(result))
