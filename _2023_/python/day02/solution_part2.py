input = open("input", "r")

line_list = input.readlines()


def format_input(line_list):
    input_lines = []
    x = 1
    for line in line_list:
        line = line.replace(f"Game {x}: ", "").replace(", ", ",")
        line = line.replace("; ", ";")
        line = line.replace("\n", "")
        input_lines.append(line)
        x += 1
    return input_lines


def get_games(input_lines):
    games = []
    for line in input_lines:
        bags = []
        for bag in line.split(";"):
            bags.append(get_dict_from_bag(bag))
        games.append(bags)

    return games


def get_dict_from_bag(bag):
    dict = {}
    for ball in bag.split(","):
        temp = ball.split(" ")
        dict.update({temp[1]: int(temp[0])})

    if "blue" not in dict.keys():
        dict.update({"blue": 0})
    if "green" not in dict.keys():
        dict.update({"green": 0})
    if "red" not in dict.keys():
        dict.update({"red": 0})

    return dict


def rgb_list(game):
    rgb_list = [[], [], []]
    for set in game:
        rgb_list[0].append(set["red"])
        rgb_list[1].append(set["green"])
        rgb_list[2].append(set["blue"])
    rgb_list[0].sort()
    rgb_list[1].sort()
    rgb_list[2].sort()

    return rgb_list


def rgb_list_from_games(games):
    list = []
    for game in games:
        list.append(rgb_list(game))
    return list


def get_power(list):
    return list[0][-1] * list[1][-1] * list[2][-1]


def get_power_sum(rgb_list):
    acc = 0
    for set in rgb_list:
        acc += get_power(set)
    return acc


input_lines = format_input(line_list)

games = get_games(input_lines)

for y in games:
    print(y)

rgb_list_for_games = rgb_list_from_games(games)

for x in rgb_list_for_games:
    print(x)

print(f"Power Sum {get_power_sum(rgb_list_for_games)}")
