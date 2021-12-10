with open("./data-test.txt") as f:
    lines = list(map(str.strip, f.readlines()))


def parse(line: str):
    start = ["(", "[", "{", "<"]
    end = [")", "]", "}", ">"]

    stack = []

    for c in line:
        if c in start:
            stack.append(c)
        if c in end:
            last = stack.pop()
            if start.index(last) != end.index(c):
                # return  [3, 57, 1197, 25137][end.index(c)]
                return 0

    score = 0
    for c in reversed(stack):
        score = (score * 5) + [1, 2, 3, 4][start.index(c)]

    return score


scores = [parse(line) for line in lines]
scores = [score for score in scores if score != 0]
print(sorted(scores)[len(scores)//2])
