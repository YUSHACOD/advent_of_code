input = open("input", "r")

line_list = input.readlines()


def ints_from_string(charachters):
    int_list = []
    for c in charachters:
        if str.isdigit(c):
            int_list.append(int(c))
    return int_list


def int_list_from_lines(line_list):
    int_list = []
    for line in line_list:
        int_list.append(ints_from_string(list(line)))

    return int_list


def create_num(a, b):
    return int(str(a) + str(b))


def sum_of_last_and_first(int_list):
    answer = 0
    for integers in int_list:
        answer += create_num(integers[0], integers[-1])

    return answer


integer_list = int_list_from_lines(line_list)

print(sum_of_last_and_first(integer_list))
