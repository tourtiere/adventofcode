def load_file(filename):
    file = open(filename, "r")
    lines = file.read()
    lines = lines.split("\n")
    file.close()
    return lines

def problem_a(n:int):
    lines = load_file("./data.txt")
    bits = []
    for i in range(len(lines[0])):
        splits = split_bits(lines, i)

        bit = 1 if (len(splits[1]) > len(splits[0])) else 0
        if (n == 0):
            bit = [1,0][bit]

        bits += [bit]
    return "".join([str(b) for b in bits])


def split_bits(lines:list[str], i:int) :
    zeros = [line for line in lines if line[i] == "0"]
    ones = [line for line in lines if line[i] == "1"]
    return zeros, ones 

def problem_b(n:int):
    lines = load_file("./data.txt")
    not_n =[1,0][n]
    for i in range(len(lines[0])):
        splits = split_bits(lines, i)

        if len(splits[n]) > len(splits[not_n]):
            lines = splits[1]
        elif len(splits[n]) < len(splits[not_n]):
            lines = splits[0]
        else:
            lines = splits[n]

        if len(lines) == 1:
            return lines[0]
    return ""



if __name__ == "__main__":
    print("problem a")

    a1 = int(problem_a(0), 2)
    a2 = int(problem_a(1), 2)

    print(a1 * a2)
    
    o2 = int(problem_b(1), 2)
    co2 = int(problem_b(0), 2)
    #b2 = int(problem_b(1), 2)
    print(o2* co2)
