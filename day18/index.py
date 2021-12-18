import math
with open("./data.txt") as f:
    arr = [eval(i) for i in f.read().split("\n")[:-1]]

good_path = []
ordered_paths = []
popped = []


def explode_locate(exp, path):
    global good_path, popped

    if isinstance(exp, int):
        return None

    if (isinstance(exp, list)):
        left, right = exp

        if len(path) >= 4 and good_path == [] and isinstance(left, int) and isinstance(right, int):
            good_path = path
            popped = exp
            return

        explode_locate(left, path + [0])
        explode_locate(right, path + [1])

    return exp


def list_paths(exp, path):
    global ordered_paths, good_path

    if path == good_path:
        ordered_paths.append(path)
        return

    if isinstance(exp, list):
        left, right = exp
        list_paths(left, path + [0])
        list_paths(right, path + [1])
        return

    ordered_paths.append(path)


def zero_paths(exp, path):
    global popped

    if (path == good_path):
        return 0

    if isinstance(exp, list):
        left, right = exp
        return [zero_paths(left, path + [0]), zero_paths(right, path + [1])]
    else:
        return exp


has_split = False


def split(exp):
    global has_split

    if isinstance(exp, list):
        left, right = exp
        return [split(left), split(right)]
    else:
        if (exp >= 10 and not has_split):
            has_split = True
            res = [exp // 2, (exp+1) // 2]
            return res
        return exp


def add_n(exp, path, ref_path, n):
    if isinstance(exp, list):
        left, right = exp
        return [add_n(left, path + [0], ref_path, n), add_n(right, path + [1], ref_path, n)]
    else:
        if (path == ref_path):
            return exp + n
        return exp


def explode(exp):
    global good_path, ordered_paths, popped

    good_path = []
    ordered_paths = []
    popped = []
    explode_locate(exp, [])

    if (good_path == []):
        return exp

    list_paths(exp, [])

    if (len(popped) == 0):
        return exp

    exp = zero_paths(exp, [])
    z = ordered_paths.index(good_path)
    if (z - 1) >= 0:
        exp = add_n(exp, [], ordered_paths[z-1], popped[0])
    if (z + 1) < len(ordered_paths):
        exp = add_n(exp, [], ordered_paths[z+1], popped[1])

    return exp


def check_magnitude(exp):

    if isinstance(exp, list):
        left, right = exp
        return 3*check_magnitude(left) + 2*check_magnitude(right)
    else:
        return exp


def loop_explode(exp):
    last_exp = []
    while exp != last_exp:
        last_exp = exp
        exp = explode(exp)
    return exp


def loop_split(exp):
    last_exp = []
    while exp != last_exp:
        last_exp = exp
        exp = split(exp)
    return exp


def add(a, b):
    global has_split
    last_exp = []
    exp = [a, b]

    while exp != last_exp:
        last_exp = exp
        exp = loop_explode(exp)
        has_split = False
        exp = split(exp)
    return exp


# problem a
s = arr[0]
for i in arr[1:]:
    s = add(s, i)
print(check_magnitude(s))


m = 0
for i in arr:
    for j in arr:
        mag = check_magnitude(add(i, j))
        if mag > m:
            m = mag
print(m)
