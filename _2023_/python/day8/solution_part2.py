# PARSING ###############################
from math import lcm
from functools import reduce

file = open("input", "r")


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
def find_lcm(list):
    x = reduce(lcm, list)
    return x


def get_list_ending_with_a(route_list):
    output = []

    for route in route_list:
        if route[-1] == 'A':
            output.append(route)

    return output


def get_list_ending_with_z(route_list):
    output = []

    for route in route_list:
        if route[-1] == 'Z':
            output.append(route)

    return output


def get_new_routes(direction, route_list, routes):
    output = []

    for route in route_list:
        output.append(routes[route][direction])

    return output


def get_steps(instructions, routes, next, steps):
    acc = 0

    number_of_instruction = len(instructions)

    while True:
        if next[-1] == 'Z':
            break
        else:
            next = routes[next][instructions[steps]]
            acc += 1
            steps = (steps + 1) % number_of_instruction

    return (acc, steps, next)


def get_steps_to_reach_Z_and_back_to_Z(instructions, routes, start_list):
    steps = []

    for start in start_list:
        to_Z, step, next = get_steps(instructions, routes, start, 0)

        steps.append(to_Z)

    return steps
#########################################


# SOLUTION ##############################
instructions, routes = input

print(f"Instructions : {instructions}")

for route in routes:
    print(f"{route} : {routes[route]}")

start_list = get_list_ending_with_a(routes)
print(f"List of routes ending with \'A\' : {start_list}")

print(f"List of routes ending with \'Z\' : {get_list_ending_with_z(routes)}")

steps = get_steps_to_reach_Z_and_back_to_Z(instructions, routes, start_list)
print(steps)

print(find_lcm(steps))
#########################################
