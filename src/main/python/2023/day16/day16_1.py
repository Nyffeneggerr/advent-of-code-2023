from collections import deque

beam_queue = deque()
energized_tiles = set()
seen_directions = list()
x_max = 0
y_max = 0
max_energize = 0


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def get_tile(x, y, data):
    data_line = data[y]
    return data_line[x]


def boundary_check(x, y):
    return 0 <= x < x_max and 0 <= y < y_max


def add_to_queue_if_ok(x, y, dr):
    combination = str(x) + ':' + str(y) + ':' + str(dr)

    if combination in seen_directions:
        return

    if boundary_check(x, y):
        beam_queue.append(combination)
        seen_directions.append(combination)


def treat_as_air(x, y, dr):
    if dr == 0:
        x += 1
    elif dr == 1:
        y += 1
    elif dr == 2:
        x -= 1
    elif dr == 3:
        y -= 1

    add_to_queue_if_ok(x, y, dr)


def print_map():
    for y in range(0, y_max):
        line = ''

        for x in range(0, x_max):
            if (str(x) + ':' + str(y)) in energized_tiles:
                line += '#'
            else:
                line += '.'

        print(line)


# directions:
# 0: right
# 1: down
# 2: left
# 3: up
if __name__ == '__main__':
    data = read_data()

    x_max = len(data[0])
    y_max = len(data)

    # for row in range(0, y_max):
    #     current_combination = str(x_max - 1) + ':' + str(row) + ':2'
    # for row in range(0, y_max):
    #     current_combination = '0:' + str(row) + ':0'
    # for row in range(0, y_max):
    #     current_combination = str(row) + ':0:1'
    for row in range(0, y_max):
        current_combination = str(row) + ':' + str(x_max - 1) + ':3'

        energized_tiles = set()
        seen_directions = list()

        beam_queue.append(current_combination)
        seen_directions.append(current_combination)

        while len(beam_queue) > 0:
           queue_entry = beam_queue.popleft()

           x, y, dr = queue_entry.split(':', 3)
           x = int(x)
           y = int(y)
           dr = int(dr)

           energized_tiles.add(str(x) + ':' + str(y))

           tile = get_tile(x,y,data)

           if tile == '.':
               treat_as_air(x, y, dr)
           elif tile == '-':
               if dr == 0 or dr == 2:
                   treat_as_air(x, y, dr)
               else:
                   add_to_queue_if_ok(x - 1, y, 2)
                   add_to_queue_if_ok(x + 1, y, 0)
           elif tile == '|':
               if dr == 1 or dr == 3:
                   treat_as_air(x, y, dr)
               else:
                   add_to_queue_if_ok(x, y - 1, 3)
                   add_to_queue_if_ok(x, y + 1, 1)
           elif tile == '/':
               if dr == 0:
                   add_to_queue_if_ok(x, y - 1, 3)
               elif dr == 1:
                   add_to_queue_if_ok(x - 1, y, 2)
               elif dr == 2:
                   add_to_queue_if_ok(x, y + 1, 1)
               elif dr == 3:
                   add_to_queue_if_ok(x + 1, y, 0)
           elif tile == '\\':
               if dr == 0:
                   add_to_queue_if_ok(x, y + 1, 1)
               elif dr == 1:
                   add_to_queue_if_ok(x + 1, y, 0)
               elif dr == 2:
                   add_to_queue_if_ok(x, y - 1, 3)
               elif dr == 3:
                   add_to_queue_if_ok(x - 1, y, 2)

        # print_map()
        energized_tiles_count = len(energized_tiles)
        print('Row: ' + str(row) + ' / tiles: ' + str(energized_tiles_count))

        if energized_tiles_count > max_energize:
            max_energize = energized_tiles_count

    print('max: ' + str(max_energize))



