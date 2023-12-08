
def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def get_maps(data):
    maps = {}
    for line in data:
        maps[line[0:3]] = [line[7:10], line[12:15]]

    return maps


def follow_the_path(instructions, maps):
    current_node = maps['AAA']
    number_of_jumps = 0
    string_index = 0

    while (True):
        path = instructions[string_index]

        if path == 'L':
            next_node_string = current_node[0]
        else:
            next_node_string = current_node[1]

        number_of_jumps += 1

        if next_node_string == 'ZZZ':
            return number_of_jumps

        current_node = maps[next_node_string]

        string_index += 1

        if string_index >= len(instructions):
            string_index = 0


if __name__ == '__main__':
    data = read_data()

    instructions = data[0]
    maps = get_maps(data[2:])

    result = follow_the_path(instructions, maps)
    print(result)
