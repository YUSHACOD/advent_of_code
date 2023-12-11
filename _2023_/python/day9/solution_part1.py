# PARSING ###############################
file = open("input", "r")


def parse_int_from_(line):
    output = []

    line = line.replace("\n", "").split(" ")
    for integer in line:
        output.append(int(integer))

    return output


def parse_input(file):
    output = []

    lines = file.readlines()

    for line in lines:
        output.append(parse_int_from_(line))

    return output


input = parse_input(file)
#########################################


# SOLUTION FUNCTIONS ####################
def all_are_zero(integers):

    for integer in integers:
        if integer != 0:
            return False
        else:
            continue

    return True


def difference_list(integers):

    length = len(integers) - 1
    output = []

    for index in range(length):
        output.append(integers[index + 1] - integers[index])

    return output


def calculate_prediction(history):
    history = history[::-1]
    length = len(history)

    acc = 0
    for index in range(length):
        acc += history[index][-1]

    return acc


def get_prediction_aux(history):
    print(f"History : {history}")
    if all_are_zero(history[-1]):
        return calculate_prediction(history)
    else:
        history.append(difference_list(history[-1]))
        return get_prediction_aux(history)


def get_prediction(readings):
    return get_prediction_aux([readings])
#########################################


# SOLUTION ##############################
print(input)

acc = 0
for readings in input:
    print(f"{readings} : {get_prediction(readings)}")
    acc += get_prediction(readings)

print(f"Answer : {acc}")
#########################################
