import math


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def get_maps(data):
    maps = {}
    for line in data:
        maps[line[0:3]] = [line[7:10], line[12:15]]

    return maps


def get_starting_nodes(maps):
    nodes = []
    for key in maps.keys():
        if key[2] == 'A':
            nodes.append(maps[key])

    return nodes


def follow_the_path(instructions, maps, current_node):
    number_of_jumps = 0
    string_index = 0

    while (True):
        path = instructions[string_index]

        if path == 'L':
            next_node_string = current_node[0]
        else:
            next_node_string = current_node[1]

        number_of_jumps += 1

        if next_node_string[2] == 'Z':
            return number_of_jumps

        current_node = maps[next_node_string]

        string_index += 1

        if string_index >= len(instructions):
            string_index = 0


def get_all_the_lowest_numbers(instructions, maps):
    current_nodes = get_starting_nodes(maps)
    print(current_nodes)
    result = []

    for current_node in current_nodes:
        result.append(follow_the_path(instructions, maps, current_node))

    return result


if __name__ == '__main__':
    data = read_data()

    instructions = data[0]
    maps = get_maps(data[2:])

    result = get_all_the_lowest_numbers(instructions, maps)
    print(result)
    print(math.lcm(*result))

