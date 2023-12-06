times = [44, 89, 96, 91]
distances = [277, 1136, 1890, 1768]

# times = [7,15,30]
# distances = [9, 40, 200]

results = []

for time, dist in zip(times, distances):
    count = 0
    for speed in range(time):
        if speed * (time - speed) > dist:
            count += 1
    results.append(count)

# x * time - x^2 = distance
