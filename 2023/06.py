def roots_quadratic(a,b,c):
    d = (b**2-4*a*c)**0.5
    return ((-b + d )/ (2*a), (-b - d )/ (2*a))

def fn(time, distance):
    a, b = roots_quadratic(-1, time, -distance)
    count = (int(b) - int(a))
    return count

with open("./data.txt") as f:
    content = f.read() 
    lines = content.split("\n")
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]

    part1 = 1
    for time, distance in zip(times, distances):
        part1 *= fn(int(time), int(distance))
    print(part1)

    time = int("".join(times))
    distance = int("".join(distances))
    print(fn(time,distance))
