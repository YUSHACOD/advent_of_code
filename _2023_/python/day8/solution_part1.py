# PARSING ###############################
file = open("input_test", "r")


def parse_instructions(inst):
    output = []
    for x in inst:
        if x == 'L':
            output.append(0)
        elif x == 'R':
            output.append(1)
        else:
            continue

    return output


def parse_routes(routes):
    dictionary = {}
    for route in routes:
        route = route.replace("\n", "")
        route = route.replace(" = (", ",")
        route = route.replace(", ", ",")
        route = route.replace(")", "")
        route = route.split(",")
        dictionary.update({route[0]: [route[1], route[2]]})

    return dictionary


def parse_input(file):

    lines = file.readlines()

    instructions = parse_instructions(lines[0].replace("\n", ""))
    routes = parse_routes(lines[2::])

    return (instructions, routes)


input = parse_input(file)
#########################################


# SOLUTION FUNCTIONS ####################
def get_steps(instructions, routes):
    acc = 0

    number_of_instruction = len(instructions)
    steps = 0
    next = 'AAA'

    while True:
        if next == 'ZZZ':
            break
        else:
            next = routes[next][instructions[steps]]
            print(f"Next : {next}")
            acc += 1
            steps = (steps + 1) % number_of_instruction

    return acc
#########################################


# SOLUTION ##############################
instructions, routes = input

print(f"Instructions : {instructions}")

print(f"Routes : {routes}")

print(f"Answer : {get_steps(instructions, routes)}")
#########################################
