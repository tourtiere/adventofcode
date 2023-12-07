from collections import defaultdict

def get_score(hand):
    m = defaultdict(int)
    for i in hand:
        m[i] += 1
    v = sorted(m.values())
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

    cards = "23456789TJQKA"
    for i in hand:
        score = score * len(cards) + cards.index(i)

    return score


with open("./data.txt") as f:
    content = f.read() 
    lines = content.split("\n")
    hand_bids = [line.split() for line in lines]
    hand_bids = sorted(hand_bids, key=lambda hand_bids: get_score(hand_bids[0]))
    bids = [ (i +1) * int(handbid[1]) for i, handbid in enumerate(hand_bids)]
    print(sum(bids))
