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
    return wins


card_counts = [1 for x in range(len(cards))]

print(card_counts)
print("")


def increase_card_counts(start, end):
    while start < end:
        if start >= len(cards):
            break
        card_counts[start] += 1
        start += 1


def get_total_scorecards(cards):
    length = len(cards)
    for x in range(0, length):
        for j in range(card_counts[x]):
            start = x + 1
            end = start + get_score(cards[x])
            increase_card_counts(start, end)



get_total_scorecards(cards)

result = 0

for x in card_counts:
    result += x

print(result)
