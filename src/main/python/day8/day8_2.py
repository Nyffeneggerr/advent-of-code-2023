
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


def follow_the_path(instructions, maps):
    current_nodes = get_starting_nodes(maps)
    print(current_nodes)
    number_of_jumps = 0
    string_index = 0

    while (True):
        path = instructions[string_index]

        finished = True

        if path == 'L':
            for index, current_node in enumerate(current_nodes):
                next_node_string = current_node[0]

                if next_node_string[2] != 'Z':
                    finished = False

                current_nodes[index] = maps[next_node_string]
        else:
            for index, current_node in enumerate(current_nodes):
                next_node_string = current_node[1]

                if next_node_string[2] != 'Z':
                    finished = False

                current_nodes[index] = maps[next_node_string]

        number_of_jumps += 1

        if finished:
            return number_of_jumps

        string_index += 1

        if string_index >= len(instructions):
            string_index = 0


if __name__ == '__main__':
    data = read_data()

    instructions = data[0]
    maps = get_maps(data[2:])

    result = follow_the_path(instructions, maps)
    print(result)
