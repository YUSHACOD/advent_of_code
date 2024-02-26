# PARSING ###############################
file = open("input_test1", "r")


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
#########################################


# SOLUTION ##############################
print(input)
#########################################
