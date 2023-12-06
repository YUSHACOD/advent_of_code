import re
input_file = open("input", "r")

lines = input_file.readlines()


def parse_input(lines):
    output = []
    length = len(lines)
    x = 0
    for y in range(length):
        lines[x] = lines[x].split(": ")[1]
        lines[x] = lines[x].replace("\n", "")
        output.append(lines[x].split(" | "))
        x += 1

    return output


lines = parse_input(lines)


def get_nums(line):
    output = []
    nums = re.split(r"\s+", line.strip())
    for x in nums:
        output.append(int(x.strip()))

    return output


def get_cards(lines):
    output = []
    for line in lines:
        output.append([get_nums(line[0]), get_nums(line[1])])

    return output


cards = get_cards(lines)


def get_score(card):
    winning_number = set(card[0])
    my_number = set(card[1])
    wins = len(winning_number.intersection(my_number))
    if wins > 0:
        return 2 ** (wins - 1)
    else:
        return 0


def get_total_score(cards):
    acc = 0
    for card in cards:
        acc += get_score(card)

    return acc


print(get_total_score(cards))
