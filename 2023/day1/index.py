with open("./data.txt") as f:
    lines = f.readlines()
    chiffres = '0123456789'
    lettres = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    s1 = 0
    s2 = 0
    for line in lines:
        # premiere partie
        line_chiffres = [i for i in line if i in chiffres]
        a, b = int(line_chiffres[0]), int(line_chiffres[-1])
        s1 += a * 10 + b

        # deuxieme partie
        line_chiffres = []
        for i in range(len(line)):
            for j in range(10):
                if (chiffres[j] == line[i]):
                    line_chiffres.append(j)
                subline = line[i:]
                if (len(subline) >= len(lettres[j])):
                    if (subline[:len(lettres[j])] == lettres[j]):
                        line_chiffres.append(j)
        a, b = int(line_chiffres[0]), int(line_chiffres[-1])
        s2 += a * 10 + b
    print(s1)
    print(s2)
