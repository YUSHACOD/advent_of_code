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
def print_map(map):
    new_map = []
    for line in map:
        x = ''
        for point in line:
            x = x + point
        new_map.append(x)

    for line in new_map:
        print(line)


def is_line_empty(line):
    for point in line:
        if point == '#':
            return False
        else:
            continue
    return True


def expand(map):
    new_map = []
    for line in map:
        if is_line_empty(line):
            new_map.append(line)
        else:
            new_map.append(line)

    return new_map


def transpose(map):
    leny = len(map)
    lenx = len(map[0])
    new_map = [['*' for y in range(leny)] for x in range(lenx)]
    for y in range(leny):
        for x in range(lenx):
            new_map[x][y] = map[y][x]

    return new_map


def construct_true_map(map):
    true_map = []

    galaxy_counter = 1

    for line in map:
        true_line = []
        for point in line:
            if point == '#':
                true_line.append(('#', galaxy_counter))
                galaxy_counter += 1
            else:
                true_line.append(('.'))

        true_map.append(true_line)

    return true_map


def get_all_edges_between_galaxies(map):
    edges = set()
    y, x = 0, 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x][0] == '#':
                j, i = 0, 0
                for j in range(len(map)):
                    for i in range(len(map[j])):
                        if map[j][i][0] == '#':
                            if map[y][x][1] > map[j][i][1]:
                                if not (y == j and x == i):
                                    edges.add((map[y][x][1], map[j][i][1],
                                               (y + 1, x + 1), (j + 1, i + 1)))
                            else:
                                if not (y == j and x == i):
                                    edges.add((map[j][i][1], map[y][x][1],
                                               (j + 1, i + 1), (y + 1, x + 1)))

    return edges


def calculate_expansion_overhead(point_a, point_b, map):
    expansion = 1000000
    overhead = 0

    y, x = point_a
    j, i = point_b
    y -= 1
    x -= 1
    j -= 1
    i -= 1

    a, b = 0, 0

    if y > j:
        b, a = y, j
    else:
        a, b = y, j

    x_expansion = 0

    for index in range(a, b):
        if is_line_empty(map[index]):
            x_expansion += 1

    map = transpose(map)

    y_expansion = 0

    a, b = 0, 0

    if x > i:
        b, a = x, i
    else:
        a, b = x, i

    for index in range(a, b):
        if is_line_empty(map[index]):
            y_expansion += 1

    overhead = (x_expansion + y_expansion) * (expansion - 1)

    return overhead


def get_sum_of_minimum_distances(edges, map):
    acc = 0

    for edge in edges:
        acc += abs(edge[2][0] - edge[3][0]) + abs(edge[2][1] - edge[3][1])
        over = calculate_expansion_overhead(edge[2], edge[3], map)
        acc += over

    return acc
#########################################


# SOLUTION ##############################
map = input


true_map = construct_true_map(map)
# for line in true_map:
#    print(line)


edges = get_all_edges_between_galaxies(true_map)

print("++++++++++++++++++++")

# for x in edges:
#     print(x)

print(len(edges))

print("++++++++++++++++++++")

print(f"Answer : {get_sum_of_minimum_distances(edges, map)}")
#########################################
