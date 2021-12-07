import re


def parse():
    with open('data-test.txt') as f:
        content = f.read()
        picks = [int(x) for x in re.findall("\\d+", content.split("\n")[0])]
        squares = [
            [
                [int(x) for x in re.findall("\\d+", line[0])]
                for line in re.findall("((\\d+ *){5}\\n)", square[0])
            ]
            for square in re.findall("(((\\d+ *){5}\\n\\s*){5})", content, re.MULTILINE)
        ]
    return picks, squares


def check_bingo(picks: list[int], square: list[list[int]]) -> bool:
    def check_line(line):
        return len([x for x in line if x in picks]) == 5

    # horizontal check
    for line in square:
        if check_line(line):
            return True

    # vertical check
    for i in range(len(square)):
        line = [horizontal[i] for horizontal in square]
        if check_line(line):
            return True

    return False


def play(picks, squares):
    for i in range(len(picks)):
        sub_picks = picks[0:i]
        for square in squares:
            if(check_bingo(sub_picks, square)):
                return sub_picks, square
                return sub_picks, square


def play_loser_is_winner(picks, squares):
    winners = [False for _ in squares]
    for i in range(len(picks)):
        sub_picks = picks[0:i]
        for i, square in enumerate(squares):
            if winners[i]:

                continue

            if(check_bingo(sub_picks, square)):
                winners[i] = True
                if winners.count(True) == len(squares):
                    return sub_picks, square


def day4():

    picks, squares = parse()

    print(picks, squares)
    res = play_loser_is_winner(picks, squares)
    if (res is not None):
        winner_picks, winner_square = res
        flatten_square = [x for line in winner_square for x in line]
        unmarked = [x for x in flatten_square if x not in winner_picks]

        print(sum(unmarked) * winner_picks[-1])


if __name__ == "__main__":
    day4()
