# PARSING ###############################
import functools
file = open("input", "r")


def parse_input(file):

    lines = file.readlines()

    output = []
    for line in lines:
        line = line.replace("\n", "").strip()
        line = line.split(" ")
        line[1] = int(line[1])
        output.append(line)

    return output


input = parse_input(file)
#########################################


# SOLUTION FUNCTIONS ####################
def get_card_values(card):
    match card:
        case 'A':
            return 0

        case 'K':
            return 1

        case 'Q':
            return 2

        case 'J':
            return 13

        case 'T':
            return 4

        case '9':
            return 5

        case '8':
            return 6

        case '7':
            return 7

        case '6':
            return 8

        case '5':
            return 9

        case '4':
            return 10

        case '3':
            return 11

        case '2':
            return 12

        case _:
            return -1


def cards_compare(hand_a, hand_b):
    for x in range(5):
        cmp = get_card_values(hand_b[x]) - get_card_values(hand_a[x])
        if cmp == 0:
            continue
        else:
            if cmp > 0:
                return 1
            else:
                return -1
    return 0


def get_dict(hand):
    cards = {}
    set_cards = list(set(hand))
    for x in set_cards:
        cards.update({x: 0})
    hand = list(hand)
    for x in hand:
        cards[x] += 1

    return cards


def j_check(hand):
    dic = get_dict(hand)
    keys = dic.keys()
    highest = ''
    values = dic.values()
    values = list(values)
    values.sort()
    high_index = values[-1]
    for x in keys:
        if dic[x] == high_index:
            if x != 'J':
                highest = x
                break

    print(f"{hand} : {dic} : {highest}")

    return hand.replace('J', highest)


def get_kind(hand):
    if 'J' in hand:
        hand = j_check(hand)
    length = len(set(hand))
    match length:
        case 1:
            return 1

        case 2:
            values = get_dict(hand).values()
            if 1 in values:
                return 2
            else:
                return 3

        case 3:
            values = get_dict(hand).values()
            if 2 not in values:
                return 4
            else:
                return 5

        case 4:
            return 6

        case 5:
            return 7
    return 1


def hand_compare(hand_a, hand_b):
    cmp = get_kind(hand_b) - get_kind(hand_a)

    if cmp == 0:
        return 0
    elif cmp > 0:
        return 1
    else:
        return -1


def compare_aux(hand_a, hand_b):
    match hand_compare(hand_a, hand_b):
        case 0:
            return cards_compare(hand_a, hand_b)

        case  1:
            return 1

        case -1:
            return -1

        case _:
            return 0


def compare(x, y):
    return compare_aux(x[0], y[0])
#########################################


# SOLUTION ##############################
print(input)

hands = sorted(input, key=functools.cmp_to_key(compare))

print(hands)

acc = 0
length = len(hands)
for index in range(length):
    acc += (index + 1) * hands[index][1]

print(f"Answer {acc}")
#########################################
