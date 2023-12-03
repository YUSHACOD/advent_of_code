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


def game_is_valid(game):
    flag = True
    for set in game:
        if set["blue"] <= 14 and set["green"] <= 13 and set["red"] <= 12:
            flag = True
        else:
            flag = False
            break

    return flag


def count_of_valid_games(games):
    count = 0
    for index in range(len(games)):
        if game_is_valid(games[index]):
            print(f"Index : {index + 1}")
            count += index + 1

    return count


input_lines = format_input(line_list)

games = get_games(input_lines)

for y in games:
    print(y)

print(f"Valid game count : {count_of_valid_games(games)}")
