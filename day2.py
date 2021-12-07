def load_file(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    return lines

def day2():
    path = "./data/day2.txt"
    lines = load_file(path)
    x = 0
    y = 0
    aim = 0
    for line in lines:
        subs = line.split(" ")
        [t, n ] = subs
        n = int(n)
        if t == "up":
            aim -= n
        if t == "down":
            aim += n
        if t== "forward":
            x += n
            y += aim * n 


    print(x * y )


if __name__ == "__main__":
    day2()