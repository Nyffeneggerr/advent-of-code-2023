from collections import deque


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def get_pipe(x, y, data):
    data_line = data[y]
    return data_line[x]


if __name__ == '__main__':
    data = read_data()

    x = 31
    y = 25
    last_coordinate = [31, 26]
    pipe_count = 0

    pipe = get_pipe(x, y, data)

    while pipe != 'S':
        pipe_count += 1

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

        pipe = get_pipe(x, y, data)

    print((pipe_count+1)/2)