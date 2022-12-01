
def rotate_scanner(scanner,  ori):
    new_scanner = []
    for a, b, c in scanner:
        new_scanner.append([
            a * ori[0],
            b * ori[1],
            c * ori[2],
        ])

    return new_scanner


def axis_scanner(scanner,  axis):
    new_scanner = []
    for line in scanner:
        new_scanner.append([
            line[axis[0]],
            line[axis[1]],
            line[axis[2]],
        ])

    return new_scanner


def pos_diff(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def apply_offset(scanner, offset):
    new_scanner = []
    for a, b, c in scanner:
        new_scanner.append([
            a + offset[0],
            b + offset[1],
            c + offset[2],
        ])

    return new_scanner


def count_scanner1inscanner2(scanner, scanner_ref):
    assert len(scanner) > 10
    assert len(scanner_ref) > 10

    return [i in scanner_ref for i in scanner].count(True)


def match_scanners(scanner, scanner_ref):

    for pos in scanner:
        for pos_ref in scanner_ref:
            offset = pos_diff(pos_ref, pos)
            corrected_scanner1 = apply_offset(scanner, offset)
            n = count_scanner1inscanner2(corrected_scanner1, scanner_ref)
            if n > 3:
                return offset
    return None


def possible_scanners(scanner):

    orientations = [
        (1, 1, 1),
        (1, -1, 1),
        (-1, 1, 1),
        (-1, -1, 1),
        (1, 1, -1),
        (1, -1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
    ]
    axis = [
        (0, 1, 2),
        (0, 2, 1),
        (2, 1, 0),
        (1, 0, 2),
    ]

    possibles = []
    for o in orientations:
        corrected_scanner = rotate_scanner(scanner, o)
        for x in axis:
            possibles.append(axis_scanner(corrected_scanner, x))
    return possibles


def main():
    with open("./test.txt") as f:
        content = f.read()[:-1]
        scanners = [[[int(i) for i in line.split(",")] for line in scan.split("\n")[1:]]
                    for scan in content.split("\n\n")]

    scanner_refs = [scanners[0]]
    scanners = scanners[1:]

    for i in range(len(scanners)):
        scanner = scanners[i]

        if scanner == []:
            continue
        for scanner_ref in scanner_refs:
            b = False
            for corrected_scanner in possible_scanners(scanner):
                offset = match_scanners(corrected_scanner, scanner_ref)
                if offset is not None:
                    corrected = apply_offset(corrected_scanner, offset)
                    scanner_refs += [corrected]
                    scanners[i] = []
                    b = True
                    break
            if b:
                break

    scanners = [pos for sc in scanner_refs for pos in scanner]
    no_duplicates = []
    for s in scanners:
        if s not in no_duplicates:
            no_duplicates.append(s)
    print(len(no_duplicates))


main()
