input = open("input", "r")

line_list = input.readlines()

# Simple Values :
# one two three four five six seven eight nine
# Collision Values :
# oneight threeight fiveight nineight
# twone
# sevenine
# eightwo eighthree


def replace_string_wth_int(line):
    a = line
    if "oneight" in line:
        a = a.replace("oneight", "18")
    if "threeight" in line:
        a = a.replace("threeight", "38")
    if "fiveight" in line:
        a = a.replace("fiveight", "58")
    if "nineight" in line:
        a = a.replace("nineight", "98")
    if "twone" in line:
        a = a.replace("twone", "21")
    if "sevenine" in line:
        a = a.replace("sevenine", "79")
    if "eightwo" in line:
        a = a.replace("eightwo", "82")
    if "eighthree" in line:
        a = a.replace("eighthree", "83")
    if "one" in line:
        a = a.replace("one", "1")
    if "two" in line:
        a = a.replace("two", "2")
    if "three" in line:
        a = a.replace("three", "3")
    if "four" in line:
        a = a.replace("four", "4")
    if "five" in line:
        a = a.replace("five", "5")
    if "six" in line:
        a = a.replace("six", "6")
    if "seven" in line:
        a = a.replace("seven", "7")
    if "eight" in line:
        a = a.replace("eight", "8")
    if "nine" in line:
        a = a.replace("nine", "9")

    return a


def int_list_from_lines(line_list):
    int_list = []
    for line in line_list:
        int_list.append(ints_from_string(list(line)))

    return int_list


def ints_from_string(charachters):
    int_list = []
    for c in charachters:
        if str.isdigit(c):
            int_list.append(int(c))
    return int_list


def create_num(a, b):
    return int(str(a) + str(b))


def sum_of_last_and_first(int_list):
    answer = 0
    for integers in int_list:
        answer += create_num(integers[0], integers[-1])

    return answer


lines = []

for line in line_list:
    lines.append(replace_string_wth_int(line))


for line in lines:
    print(line)

integer_list = int_list_from_lines(lines)

print(sum_of_last_and_first(integer_list))
