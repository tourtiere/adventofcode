from collections import defaultdict


def get_score(hand, part2=False):

    m = defaultdict(int)
    for i in hand:
        m[i] += 1

    card_order="23456789TJQKA"

    v = sorted(m.values())

    if part2:
        card_order="J23456789TQKA"
        n = m["J"]
        m["J"] = 0
        v = sorted(m.values())
        v[-1] += n

    score = 0
    if (v[-1] == 5):
        score = 6
    elif (v[-1] == 4):
        score= 5
    elif (v[-1] == 3 and v[-2] == 2):
        score= 4
    elif (v[-1] == 3):
        score= 3
    elif (v[-1] == 2 and v[-2] == 2):
        score= 2
    elif (v[-1] == 2):
        score= 1

    for i in hand:
        score = score * len(card_order) + card_order.index(i)

    return score


with open("./data.txt") as f:
    content = f.read() 
    lines = content.split("\n")
    hands = [line.split() for line in lines]

    hands = sorted(hands, key=lambda hand: get_score(hand[0], False))
    bids = [(i +1) * int(bid) for i, (_,bid) in enumerate(hands)]
    print(sum(bids))

    hands = sorted(hands, key=lambda hand: get_score(hand[0], True))
    bids = [(i +1) * int(bid) for i, (_,bid) in enumerate(hands)]
    print(sum(bids))

