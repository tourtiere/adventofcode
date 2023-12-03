import re
import math

with open("./data.txt") as f:
    content = f.read()
    lines = content.split("\n")

    max_colors = {
        "red":12,
        "green":13,
        "blue":14,
    }

    s1 = 0
    s2 = 0
    for line in lines:
        id, game = re.findall(r'Game (\d+): (.+)', line)[0]
        valid = True

        min_colors = {
            'red':-math.inf,
            'green':-math.inf,
            'blue':-math.inf
        }
        rounds = game.split(";")
        for round in rounds:
            picks = round.split(",")
            for pick in picks:
                n, color = pick.strip().split(' ')
                n = int(n)
                if (n > max_colors[color]):
                    valid = False
                min_colors[color] = max(min_colors[color], n)

        if valid:
            s1 += int(id)
        power = min_colors["red"] * min_colors['green'] * min_colors['blue']
        s2 += power

    print(s1)
    print(s2)
