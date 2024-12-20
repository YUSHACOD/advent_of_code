input_file = open("input", "r")

lines = input_file.readlines()


def remove_endlines(lines):
    output = []
    for x in lines:
        x = x.replace("\n", "")
        output.append(x)

    return output


lines = remove_endlines(lines)


def get_num(line, index):
    result = '' + line[index]
    back = 1
    front = 1
    while (index - back) >= 0 and (line[index - back].isnumeric()):
        result = line[index - back] + result
        back += 1

    while (index + front) < len(line) and (line[index + front].isnumeric()):
        result = result + line[index + front]
        front += 1

    return int(result)


def mark_num(line, index):  # When you mark a number return the line
    back = 1
    front = 1
    while (index - back) >= 0 and (line[index - back][0].isnumeric()):
        line[index - back] = (line[index - back][0],
                              line[index - back][1], True)
        back += 1

    while (index + front) < len(line) and (line[index + front][0].isnumeric()):
        line[index + front] = (line[index + front][0],
                               line[index + front][1], True)
        front += 1

    return line


def get_parsed_line(line):
    list = []
    for index in range(len(line)):
        if line[index].isnumeric():
            list.append((line[index], get_num(line, index), False))
        else:
            list.append(tuple(line[index]))

    return list


def get_parsed_input(input_lines):
    lines = []
    for x in input_lines:
        lines.append(get_parsed_line(x))

    return lines


def check_surrounding(lines, x, y, lenx, leny, acc):
    i = j = -1
    while j >= -1 and j <= 1:
        while i >= -1 and i <= 1:
            if (x + i >= 0 and x + i < lenx) and (y + j >= 0 and y + j < leny):
                if lines[y + j][x + i][0].isnumeric():
                    print(lines[y + j][x + i])
                    if not lines[y + j][x + i][2]:
                        print(lines[y + j][x + i][1])
                        acc += lines[y + j][x + i][1]
                        lines[y + j] = mark_num(lines[y + j], x + i)
            i += 1
        i = -1
        j += 1

    return (lines, acc)


def get_partNum_sum(lines):
    acc = 0
    x = y = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if not lines[y][x][0].isnumeric() and lines[y][x][0] != '.':
                lines, acc = check_surrounding(
                    lines, x, y, len(lines[y]), len(lines), acc)

    return acc


lines = get_parsed_input(lines)

print(get_partNum_sum(lines))
