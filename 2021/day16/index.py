from typing import Optional


def hex_to_bin(content: str):
    hex_map = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    return "".join([hex_map[i] for i in content])


with open("./data.txt") as f:
    content = f.read()
    content = content[:-1]


def eat(packet, i):
    return packet[:i], packet[i:]


Packet = int


def operation(type_id: int, args: list[int]):
    if type_id == 0:
        return sum(args)
    if type_id == 1:
        p = 1
        for n in args:
            p *= n
        return p
    if type_id == 2:
        return min(args)

    if type_id == 3:
        return max(args)

    if type_id == 5:
        if args[0] > args[1]:
            return 1
        else:
            return 0

    if type_id == 6:
        if args[0] < args[1]:
            return 1
        else:
            return 0

    if type_id == 7:
        if args[0] == args[1]:
            return 1
        else:
            return 0

    return 0


def parse(packet: str, limit: Optional[int]) -> tuple[list[int], str]:
    args = []

    while limit != 0 and packet != "":
        if all([p == "0" for p in packet]):
            break

        version_bit, packet = eat(packet, 3)
        version = int(version_bit, 2)

        ID_bit, packet = eat(packet, 3)
        ID = int(ID_bit, 2)

        if ID == 4:
            bits = ""
            while packet != "":
                group, packet = eat(packet, 5)
                bits += group[1:]
                if group[0] == "0":
                    break
            literal = int(bits, 2)
            args.append(literal)

        # operator
        if ID != 4:
            length, packet = eat(packet, 1)
            if length == "0":
                bits, packet = eat(packet, 15)
                sub_len = int(bits, 2)
                sub_packet, packet = eat(packet, sub_len)
                sub_args, _ = parse(sub_packet, None)
            else:

                bits, packet = eat(packet, 11)
                n_limit = int(bits, 2)
                sub_args, packet = parse(packet, n_limit)

            args.append(operation(ID, sub_args))

        if limit != None:
            limit -= 1

    return args, packet


args, packet = parse(hex_to_bin(content), None)
print(args[0])
