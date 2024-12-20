input_file = open("input2", "r")

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

maps = [
    Map(input[1]), Map(input[2]), Map(input[3]),
    Map(input[4]), Map(input[5]), Map(input[6]),
    Map(input[7])
]

seeds_mappings = []
for seed in seeds:
    global seed_mappings
    seed_mappings = [seed]
    location = seed
    for map in maps:
        seed_mappings.append(map.get_mapping(location))
        location = seed_mappings[-1]

    seeds_mappings.append(seed_mappings)

for mapping in seeds_mappings:
    print(mapping)

least = seeds_mappings[0][-1]

for x in seeds_mappings:
    if least > x[-1]:
        least = x[-1]

print(least)
