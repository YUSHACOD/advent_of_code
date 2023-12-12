# PARSING ###############################
file = open("input", "r")


def parse_input(file):
    output = []

    lines = file.readlines()

    for line in lines:
        line = line.replace("\n", "")
        output.append(list(line))

    return output


input = parse_input(file)
#########################################


# SOLUTION FUNCTIONS ####################
def get_starting_pos(map):
    y, x = 0, 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if str(map[y][x]) == 'S':
                return (y, x)

    return (y, x)


def get_valid_pos_next_to_top_left(map, my_pos, prev_pos):
    y, x = my_pos
    lengthx = len(map[y])
    lengthy = len(map)

    if (x + 1 > 0 and x + 1 < lengthx) and (y, x + 1) != prev_pos and (
            map[y][x + 1] == 'S' or
            map[y][x + 1] == '-' or
            map[y][x + 1] == '7' or
            map[y][x + 1] == 'J'):
        return (y, x + 1)

    elif (y + 1 >= 0 and y + 1 < lengthy) and (y + 1, x) != prev_pos and (
            map[y + 1][x] == 'S' or
            map[y + 1][x] == '|' or
            map[y + 1][x] == 'J' or
            map[y + 1][x] == 'L'):
        return (y + 1, x)

    else:
        return (y, x)


def get_valid_pos_next_to_vertical_bar(map, my_pos, prev_pos):
    y, x = my_pos
    lengthy = len(map)

    if (y - 1 >= 0 and y - 1 < lengthy) and (y - 1, x) != prev_pos and (
            map[y - 1][x] == 'S' or
            map[y - 1][x] == '|' or
            map[y - 1][x] == 'F' or
            map[y - 1][x] == '7'):
        return (y - 1, x)

    elif (y + 1 >= 0 and y + 1 < lengthy) and (y + 1, x) != prev_pos and (
            map[y + 1][x] == 'S' or
            map[y + 1][x] == '|' or
            map[y + 1][x] == 'J' or
            map[y + 1][x] == 'L'):
        return (y + 1, x)

    else:
        return (y, x)


def get_valid_pos_next_to_top_right(map, my_pos, prev_pos):
    y, x = my_pos
    lengthx = len(map[y])
    lengthy = len(map)

    if (y + 1 >= 0 and y + 1 < lengthy) and (y + 1, x) != prev_pos and (
            map[y + 1][x] == 'S' or
            map[y + 1][x] == '|' or
            map[y + 1][x] == 'J' or
            map[y + 1][x] == 'L'):
        return (y + 1, x)

    elif (x - 1 >= 0 and x - 1 < lengthx) and (y, x - 1) != prev_pos and (
            map[y][x - 1] == 'S' or
            map[y][x - 1] == '-' or
            map[y][x - 1] == 'F' or
            map[y][x - 1] == 'L'):
        return (y, x - 1)

    else:
        return (y, x)


def get_valid_pos_next_to_horizontal_bar(map, my_pos, prev_pos):
    y, x = my_pos
    lengthx = len(map[y])

    if (x + 1 > 0 and x + 1 < lengthx) and (y, x + 1) != prev_pos and (
            map[y][x + 1] == 'S' or
            map[y][x + 1] == '-' or
            map[y][x + 1] == '7' or
            map[y][x + 1] == 'J'):
        return (y, x + 1)

    elif (x - 1 >= 0 and x - 1 < lengthx) and (y, x - 1) != prev_pos and (
            map[y][x - 1] == 'S' or
            map[y][x - 1] == '-' or
            map[y][x - 1] == 'F' or
            map[y][x - 1] == 'L'):
        return (y, x - 1)

    else:
        return (y, x)


def get_valid_pos_next_to_bot_right(map, my_pos, prev_pos):
    y, x = my_pos
    lengthx = len(map[y])
    lengthy = len(map)

    if (y - 1 >= 0 and y - 1 < lengthy) and (y - 1, x) != prev_pos and (
            map[y - 1][x] == 'S' or
            map[y - 1][x] == '|' or
            map[y - 1][x] == 'F' or
            map[y - 1][x] == '7'):
        return (y - 1, x)

    elif (x - 1 >= 0 and x - 1 < lengthx) and (y, x - 1) != prev_pos and (
            map[y][x - 1] == 'S' or
            map[y][x - 1] == '-' or
            map[y][x - 1] == 'F' or
            map[y][x - 1] == 'L'):
        return (y, x - 1)

    else:
        return (y, x)


def get_valid_pos_next_to_bot_left(map, my_pos, prev_pos):
    y, x = my_pos
    lengthx = len(map[y])
    lengthy = len(map)

    if (y - 1 >= 0 and y - 1 < lengthy) and (y - 1, x) != prev_pos and (
            map[y - 1][x] == 'S' or
            map[y - 1][x] == '|' or
            map[y - 1][x] == 'F' or
            map[y - 1][x] == '7'):
        return (y - 1, x)

    elif (x + 1 > 0 and x + 1 < lengthx) and (y, x + 1) != prev_pos and (
            map[y][x + 1] == 'S' or
            map[y][x + 1] == '-' or
            map[y][x + 1] == '7' or
            map[y][x + 1] == 'J'):
        return (y, x + 1)

    else:
        return (y, x)


def get_valid_pos_next_to_start(starting_pos, map):
    y, x = starting_pos
    length = len(map)

    if (y - 1 > 0 and y - 1 < length) and (map[y - 1][x] == '|' or
                                           map[y - 1][x] == 'F' or
                                           map[y - 1][x] == '7'):
        return (y - 1, x)

    elif (x + 1 > 0 and x + 1 < length) and (map[y][x + 1] == '-' or
                                             map[y][x + 1] == '7' or
                                             map[y][x + 1] == 'J'):
        return (y, x + 1)

    elif (y + 1 >= 0 and y + 1 < length) and (map[y + 1][x] == '|' or
                                              map[y + 1][x] == 'J' or
                                              map[y + 1][x] == 'L'):
        return (y + 1, x)

    elif (x - 1 >= 0 and x - 1 < length) and (map[y][x - 1] == '-' or
                                              map[y][x - 1] == 'F' or
                                              map[y][x - 1] == 'L'):
        return (y, x - 1)

    else:
        return (y, x)


def crawl_map(starting_pos, map):

    current_pos = get_valid_pos_next_to_start(starting_pos, map)
    prev_pos = starting_pos
    y, x = current_pos
    acc = 0
    points = []

    while True:
        y, x = current_pos
        print(f"Current Pos : {current_pos} : {map[y][x]}")
        points.append(current_pos)
        if current_pos == starting_pos:
            break
        else:
            match map[y][x]:
                case '|':
                    temp = prev_pos
                    prev_pos = current_pos
                    current_pos = get_valid_pos_next_to_vertical_bar(
                        map,
                        current_pos,
                        temp)
                    acc += 1

                case '-':
                    temp = prev_pos
                    prev_pos = current_pos
                    current_pos = get_valid_pos_next_to_horizontal_bar(
                        map,
                        current_pos,
                        temp)
                    acc += 1

                case 'F':
                    temp = prev_pos
                    prev_pos = current_pos
                    current_pos = get_valid_pos_next_to_top_left(
                        map,
                        current_pos,
                        temp)
                    acc += 1

                case '7':
                    temp = prev_pos
                    prev_pos = current_pos
                    current_pos = get_valid_pos_next_to_top_right(
                        map,
                        current_pos,
                        temp)
                    acc += 1

                case 'J':
                    temp = prev_pos
                    prev_pos = current_pos
                    current_pos = get_valid_pos_next_to_bot_right(
                        map,
                        current_pos,
                        temp)
                    acc += 1

                case 'L':
                    temp = prev_pos
                    prev_pos = current_pos
                    current_pos = get_valid_pos_next_to_bot_left(
                        map,
                        current_pos,
                        temp)
                    acc += 1

                case _:
                    break

    return (acc, points)

#########################################


# SOLUTION ##############################
map = input
print(map)

starting_pos = get_starting_pos(map)

print(f"Starting Position : {starting_pos}")
print("Next to Starting Position : " +
      f"{get_valid_pos_next_to_start(starting_pos, map)}")

acc, points = crawl_map(starting_pos, map)

print(f"Answer : {(acc + 1) / 2}")
#########################################
