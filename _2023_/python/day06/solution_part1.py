# PARSING ###############################
import re
file = open("input", "r")


def ints_of_list(list):
    output = []
    for x in list:
        output.append(int(x))

    return output


def parse_input(file):

    lines = file.readlines()

    lines[0] = lines[0].replace("Time:", "").strip()
    lines[0] = re.split(r"\s+", lines[0])

    lines[1] = lines[1].replace("Distance:", "").strip()
    lines[1] = re.split(r"\s+", lines[1])

    lines[0] = ints_of_list(lines[0])
    lines[1] = ints_of_list(lines[1])

    return lines


input = parse_input(file)
#########################################


# SOLUTION FUNCTIONS ####################
def race_is_won(hold, time, distance):
    return (time - hold) * hold > distance


def get_wins(time, distance):
    count = 0
    for hold in range(time):
        if race_is_won(hold, time, distance):
            count += 1

    return count
#########################################


# SOLUTION ##############################
Time_Limits = input[0]
Distances = input[1]

print(Time_Limits)
print(Distances)

acc = 1
for x in range(len(Time_Limits)):
    print(f"wins {x + 1} : {get_wins(Time_Limits[x], Distances[x])}")
    acc *= get_wins(Time_Limits[x], Distances[x])

print(f"Answer : {acc}")
#########################################
