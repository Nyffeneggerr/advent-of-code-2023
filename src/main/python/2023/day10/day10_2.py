from collections import deque


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def get_pipe(x, y, data):
    data_line = data[y]
    return data_line[x]


def filter_loop_pipes(loop_pipes, data):
    result_map = list()

    for y in range(0, len(data)):
        result_line = ''

        for x in range(0, len(data[y])):
            if [x, y] in loop_pipes:
                result_line += data[y][x]
            else:
                result_line += '.'

        result_map.append(result_line)

    print(result_map)
    file = open('data_result.txt', 'w')
    for line in result_map:
        file.write(f"{line}\n")
    file.close()


if __name__ == '__main__':
    data = read_data()

    # x = 4
    # y = 1
    # last_coordinate = [4, 0]
    x = 31
    y = 25
    last_coordinate = [31, 26]

    loop_pipes = list()
    pipe = get_pipe(x, y, data)
    loop_pipes.append([x, y])

    while pipe != 'S':
        next_coordinates = set()

        if pipe == '|':
            next_coordinates = [[x, y-1],[x, y+1]]
        elif pipe == '-':
            next_coordinates = [[x-1, y],[x+1, y]]
        elif pipe == 'L':
            next_coordinates = [[x, y-1],[x+1, y]]
        elif pipe == 'J':
            next_coordinates = [[x, y-1],[x-1, y]]
        elif pipe == '7':
            next_coordinates = [[x-1, y],[x, y+1]]
        elif pipe == 'F':
            next_coordinates = [[x, y+1],[x+1, y]]

        next_coordinates.remove(last_coordinate)

        last_coordinate = [x,y]

        x = next_coordinates[0][0]
        y = next_coordinates[0][1]

        loop_pipes.append([x, y])
        pipe = get_pipe(x, y, data)

    print(loop_pipes)
    filter_loop_pipes(loop_pipes, data)
