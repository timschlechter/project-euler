HIGH_CARD = 1**9
ONE_PAIR = 10**10
TWO_PAIR = 10**11
THREE_OF_A_KIND = 10**12
STRAIGHT = 10**13
FLUSH = 10**14
FULL_HOUSE = 10**15
FOUR_OF_A_KIND = 10**16
STRAIGHT_FLUSH = 10**17
ROYAL_FLUSH = 10**18


def card_value(card):
    return int({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}.get(card, card))

def hand_rank(cards):
    values = list(map(lambda c: card_value(c[0]), cards))
    values.sort()
    suits = list(map(lambda c: c[1], cards))
    same_suit = len(set(suits)) == 1
    straight = len(set(values)) == 5 and max(values) - min(values) == 4
    highest = max(values)

    count = {}
    for v in values:
        if v in count:
            count[v] += 1
        else:
            count[v] = 1
    keys = list(count.keys())

    if same_suit and values == [10, 11, 12, 13, 14]:
        return ROYAL_FLUSH

    if same_suit and straight:
        return STRAIGHT_FLUSH + highest

    if max(count.values()) == 4:
        return FOUR_OF_A_KIND + (keys[0] * 10 + keys[1] if count[keys[0]] == 4
                                 else keys[0] + keys[1] * 10)

    if len(count.keys()) == 2:
        return FULL_HOUSE + (keys[0] * 10 + keys[1] if count[keys[0]] == 3 else
                             keys[0] + keys[1] * 10)

    if same_suit:
        return FLUSH + values[0] + values[1] * 10 + values[2] * 100 + values[3] * 1000 + values[4] * 10000

    if straight:
        return STRAIGHT + highest

    if max(count.values()) == 3:
        if count[keys[0]] == 3:
            return THREE_OF_A_KIND + keys[0]
        if count[keys[1]] == 3:
            return THREE_OF_A_KIND + keys[1]
        return THREE_OF_A_KIND + keys[2]

    if len(count.keys()) == 3:
        max_pair = values[4] if count[values[4]] == 2 else values[3]
        second_pair = values[1]
        high_card = values[0]
        if high_card == second_pair:
            high_card = values[2]
        if high_card == max_pair:
            high_card = values[4]
        return TWO_PAIR + max_pair * 100 + second_pair * 10 + high_card

    if max(count.values()) == 2:
        add = 0
        multiplier = 1
        for value in values:
            if count[value] == 2:
                add += value * 1000
            else:
                add += value * multiplier
                multiplier *= 10
        return ONE_PAIR + add

    return HIGH_CARD + values[0] + values[1] * 10 + values[2] * 100 + values[3] * 1000 + values[4] * 10000


# print(hand_rank(["TH", "JH", "QH", "KH", "AH"]) == ROYAL_FLUSH)
# print(hand_rank(["3H", "4H", "5H", "6H", "7H"]) == STRAIGHT_FLUSH + 7)
# print(hand_rank(["3H", "3C", "3S", "3D", "7H"]) == FOUR_OF_A_KIND + 30 + 7)
# print(hand_rank(["3H", "3C", "3S", "4D", "4H"]) == FULL_HOUSE + 30 + 4)
# print(hand_rank(["3H", "4H", "5H", "6H", "9H"]) == FLUSH+3+40+500+6000+90000)
# print(hand_rank(["3H", "4C", "5D", "6H", "7H"]) == STRAIGHT + 7)
# print(hand_rank(["3H", "3C", "3S", "4D", "5H"]) == THREE_OF_A_KIND + 3)
# print(hand_rank(["3H", "3C", "4S", "4D", "5H"]) == TWO_PAIR + 400 + 30 + 5)
# print(hand_rank(["3H", "3C", "4S", "5D", "6H"]) == ONE_PAIR + 3000*2 + 4 + 50 + 600)
# print(hand_rank(["3H", "8C", "4S", "5D", "6H"]) == HIGH_CARD + 3 + 40 + 500 + 6000 + 80000)

player_1_wins = 0
with open('054-poker-hands.txt') as f:
    content = f.readlines()
    for line in content:
        cards = line.split()
        hand_player_1 = cards[0:5]
        hand_player_2 = cards[5:10]

        print(hand_player_1)
        print(hand_player_2)
        if hand_rank(hand_player_1) > hand_rank(hand_player_2):
            player_1_wins += 1

print(player_1_wins)