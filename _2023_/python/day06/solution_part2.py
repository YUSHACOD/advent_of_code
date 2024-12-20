# PARSING ###############################
import re
file = open("input", "r")


def parse_input(file):

    lines = file.readlines()

    lines[0] = lines[0].replace("Time:", "").strip()
    lines[0] = re.split(r"\s+", lines[0])

    lines[1] = lines[1].replace("Distance:", "").strip()
    lines[1] = re.split(r"\s+", lines[1])

    result1 = ""
    for x in lines[0]:
        result1 = result1 + x

    result2 = ""
    for x in lines[1]:
        result2 = result2 + x

    lines[0] = int(result1)
    lines[1] = int(result2)

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
Time_Limit = input[0]
Distance = input[1]

print(Time_Limit)
print(Distance)

print(f"Answer {get_wins(Time_Limit, Distance)}")
#########################################
