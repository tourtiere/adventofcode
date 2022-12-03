count = 0
with open("./data.txt") as f:
    lines = f.read().strip().split("\n")
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for line in lines:
        n = len(line)
        a,b = line[:n//2], line[n//2:]
        letter= [c for c in a if c in b][0]
        i = alphabet.index(letter) + 1
        count += i

    print(count)

    count = 0
    for i in range(len(lines)//3):
        a, b, c = lines[i*3: i*3+3]
        char = [char for char in a if char in b and char in c][0]
        i = alphabet.index(char) + 1
        count += i
    print(count)
