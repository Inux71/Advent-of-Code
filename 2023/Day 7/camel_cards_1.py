from itertools import groupby


file = open("2023/Day 7/input.txt", 'r')

priority: list[str] = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] 

five_of_a_kind: list[str] = []
four_of_a_kind: list[str] = []
full_house: list[str] = []
three_of_a_kind: list[str] = []
two_pair: list[str] = []
one_pair: list[str] = []
high_card: list[str] = []

for line in file:
    hand, rank = line.strip().split(' ')

    pairs: list[tuple] = [(el, len(list(group))) for el, group in groupby(sorted(hand))]

    # five of a kind
    if len(pairs) == 1:
        five_of_a_kind.append((hand, rank))

    # four of a kind | full house
    if len(pairs) == 2:
        # four of a kind
        if pairs[0][1] == 4 or pairs[1][1] == 4:
            four_of_a_kind.append((hand, rank))

        # full house
        else:
            full_house.append((hand, rank))

    # three of a kind | two pair
    if len(pairs) == 3:
        # three of a kind
        if pairs[0][1] == 3 or pairs[1][1] == 3 or pairs[2][1] == 3:
            three_of_a_kind.append((hand, rank))

        # two pair
        else:
            two_pair.append((hand, rank))

    # one pair
    if len(pairs) == 4:
        one_pair.append((hand, rank))

    # high card    
    if len(pairs) == 5:
        high_card.append((hand, rank))

five_of_a_kind = sorted(five_of_a_kind, key=lambda x: [priority.index(c) for c in x[0]], reverse=True)
four_of_a_kind = sorted(four_of_a_kind, key=lambda x: [priority.index(c) for c in x[0]], reverse=True)
full_house = sorted(full_house, key=lambda x: [priority.index(c) for c in x[0]], reverse=True)
three_of_a_kind = sorted(three_of_a_kind, key=lambda x: [priority.index(c) for c in x[0]], reverse=True)
two_pair = sorted(two_pair, key=lambda x: [priority.index(c) for c in x[0]], reverse=True)
one_pair = sorted(one_pair, key=lambda x: [priority.index(c) for c in x[0]], reverse=True)
high_card = sorted(high_card, key=lambda x: [priority.index(c) for c in x[0]], reverse=True)

rank: int = 1
total: int = 0

for i in high_card:
    total += int(i[1]) * rank
    rank += 1

for i in one_pair:
    total += int(i[1]) * rank
    rank += 1

for i in two_pair:
    total += int(i[1]) * rank
    rank += 1

for i in three_of_a_kind:
    total += int(i[1]) * rank
    rank += 1

for i in full_house:
    total += int(i[1]) * rank
    rank += 1

for i in four_of_a_kind:
    total += int(i[1]) * rank
    rank += 1

for i in five_of_a_kind:
    total += int(i[1]) * rank
    rank += 1

print(total)

file.close()
