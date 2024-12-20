import multiprocessing

input_file = open("input", "r")

lines = input_file.readlines()


def parse_input(lines):
    input = ""
    for x in lines:
        input = input + x
    input = input.split("\n\n")
    parsed_input = []
    for x in input:
        y = x.splitlines()
        index = 0
        for index in range(len(y)):
            y[index] = y[index].replace("\n", "")
        parsed_input.append(y)

    return parsed_input


def split_parse_int(ints):

    ints = ints.split(" ")

    ints_list = []
    for integer in ints:
        ints_list.append(int(integer))

    return ints_list


def parse_seeds(seeds):
    seeds = seeds[0].replace("seeds: ", "")
    return split_parse_int(seeds)


class Map():

    def get_name(self, map):
        return map[0].replace(":", "")

    def parse_maps(self, map):

        map.remove(map[0])

        parsed_map = []
        for mapping in map:
            parsed_map.append(split_parse_int(mapping))

        return parsed_map

    def get_mapping(self, location):
        def contains_location(mapping, location):
            return (location >= mapping[1]) and (location < (mapping[1] +
                                                             mapping[2]))

        for mapping in self.mappings:
            if contains_location(mapping, location):
                return location - mapping[1] + mapping[0]
            else:
                continue

        return location

    def __init__(self, map):
        self.name = self.get_name(map)
        self.mappings = self.parse_maps(map)


input = parse_input(lines)

seeds = parse_seeds(input[0])

index = 0
for j in range(int(len(seeds)/2)):
    seeds[index + 1] += seeds[index]
    index += 2

maps = [
    Map(input[1]), Map(input[2]), Map(input[3]),
    Map(input[4]), Map(input[5]), Map(input[6]),
    Map(input[7])
]


def get_least(start, end, least_list):

    location = start
    for map in maps:
        location = map.get_mapping(location)
    least = location

    while start < end:

        location = start
        for map in maps:
            location = map.get_mapping(location)

        if least > location:
            least = location

        start += 1

    print(least)

    least_list.append(least)


if __name__ == "__main__":
    # Number of processes to create
    num_processes = int(len(seeds)/2)

    # Values to be processed
    values_to_process = [1, 2, 3, 4, 5]

    # Shared list to store results
    manager = multiprocessing.Manager()
    least_list = manager.list()

    input = []
    index = 0
    for x in range(num_processes):
        input.append((seeds[index], seeds[index + 1], least_list))
        index += 2

    print(seeds)
    print(input)

    # Create a pool of worker processes
    with multiprocessing.Pool(num_processes) as pool:
        # Use starmap to pass multiple arguments to the worker function
        pool.starmap(get_least, input)

    # Print the results
    least_list.sort()
    print("Results:", least_list[0])
