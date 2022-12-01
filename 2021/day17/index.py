

#target_x, target_y = list(range(20, 30 + 1)), list(range(-10, -5 + 1))
target_x, target_y = list(range(155, 182 + 1)), list(range(-117, -67 + 1))

n = abs(min(target_y) + 1)
problem_a = n * (n+1) // 2
print(problem_a)

# target area: x=20..30, y=-10..-5

y_extremum = max(abs(min(target_y)), abs(max(target_y)))
x_extremum = max(abs(min(target_x)), abs(max(target_x)))


def trajectory_x(v):
    x = 0
    steps = [x]
    while x <= max(target_x) and v != 0:
        x += v
        steps.append(x)
        if v < 0:
            v += 1
        elif v > 0:
            v -= 1
    return steps


def trajectory_y(v):
    y = 0
    steps = [y]
    while y >= min(target_y):
        y += v
        v -= 1
        steps.append(y)
    return steps


x_candidates = []
for v in range(x_extremum * 2):
    traj = trajectory_x(v)
    if any([(t in target_x) for t in traj]):
        x_candidates.append(v)

y_candidates = []
for v in range(-y_extremum * 2, y_extremum * 2):
    traj = trajectory_y(v)
    if any([(t in target_y) for t in traj]):
        y_candidates.append(v)


vs = set()
count = 0
for vx in x_candidates:

    for vy in y_candidates:
        steps_x = trajectory_x(vx)
        steps_y = trajectory_y(vy)
        if len(steps_x) < len(steps_y):
            steps_x += (len(steps_y) - len(steps_x)) * 3 * [steps_x[-1]]

        if any([x in target_x and y in target_y for x, y in zip(steps_x, steps_y)]):
            count += 1

print(count)
