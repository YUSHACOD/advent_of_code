# PARSING ###############################
file = open("input", "r")


def parse_input(file):
    stack = []
    moves = []

    lines = file.readlines()

    flag = True
    for line in lines:
        if line == "\n":
            flag = False
            continue
        if flag:
            line = line.replace("\n", "")
            line = line.replace("[", " ")
            line = line.replace("]", " ")
            stack.append(line)
        else:
            moves.append(line)

    return (stack, moves)


stack, moves = parse_input(file)


def parse_moves(moves):
    result = []

    for move in moves:
        instr = []
        for x in move.split(" "):
            try:
                instr.append(int(x))
            except ValueError:
                pass

        result.append(instr)

    return result


def parse_stack(stack):
    result = []

    lengthx = int(stack[-1].replace(" ", "")[-1])
    lengthy = len(stack) - 1

    i = 1
    for _ in range(lengthx):
        result.append([])
        for j in range(lengthy):
            if stack[j][i] != ' ':
                result[-1].append(stack[j][i])
        i += 4

    print("Length: " + str(lengthx))

    return result


for x in stack:
    print(x)


"""
for x in stack:
    print(x)
print("###")
for x in moves:
    print(x)
"""
#########################################


# SOLUTION FUNCTIONS ####################
class Ship():

    def __init__(self, number_of_stack: int):
        self.stacks = [[] for _ in range(number_of_stack)]

    def pop(self, position: int):
        return self.stacks[position].pop()

    def push(self, position: int, crate):
        return self.stacks[position].append(crate)

    def apply_move(self, move):

        temp = list()

        for _ in range(move[0]):
            temp.append(self.pop(move[1] - 1))

        temp = temp[::-1]
        for x in temp:
            self.push(move[2] - 1, x)


#########################################

# SOLUTION ##############################
stack = parse_stack(stack)
moves = parse_moves(moves)

ship = Ship(len(stack))
for i in range(len(stack)):
    for x in (stack[i])[::-1]:
        ship.push(i, x)


for move in moves:
    ship.apply_move(move)
    print()
    print(move)
    for x in ship.stacks:
        print(x)
    print()

"""
for x in ship.stacks:
    print(x)
"""

result = ''
for x in ship.stacks:
    result = result + x[-1]

print(result)
#########################################
